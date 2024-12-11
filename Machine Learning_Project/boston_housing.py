# -*- coding: utf-8 -*-
"""Boston Housing

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1OqcaHDQ87vYsxcADcc0Q_dNIbJMavSOg
"""

!pip install catboost -q

import pandas as pd
import numpy as np
from scipy import stats
from sklearn import tree, ensemble
from sklearn.ensemble import AdaBoostRegressor, GradientBoostingRegressor, RandomForestRegressor
from sklearn.model_selection import KFold, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error
#from catboost import CatBoostRegressor
from google.colab import drive

import matplotlib.pyplot as plt
import seaborn as sns

# Commented out IPython magic to ensure Python compatibility.
# Mount to Google Drive
from google.colab import drive
drive.mount('/content/drive', force_remount=True)

# Define Project Folder
FOLDERNAME = 'Colab\ Notebooks/Boston\ Housing'

# %cd drive/MyDrive/$FOLDERNAME

def out_file(predictions, ids, filename):
    output = pd.DataFrame({'ID': ids, 'medv': predictions})
    output.to_csv(filename, index=False)

data = pd.read_csv('train.csv')
test_data = pd.read_csv('test.csv')
print(data.shape)
print(test_data.shape)

"""# Data Preprocessing"""

# 設置畫布大小
plt.figure(figsize=(16, 12))

# 獲取所有欄位名稱
columns = data.columns

# 計算需要的行數與列數
num_cols = 3  # 每行顯示 3 個箱型圖
num_rows = (len(columns) + num_cols - 1) // num_cols  # 計算需要的行數

# 繪製子圖
for i, column in enumerate(columns, 1):  # enumerate 從 1 開始
    plt.subplot(num_rows, num_cols, i)
    sns.boxplot(y=data[column])  # 箱型圖
    plt.title(f'Box Plot of {column}', fontsize=10)  # 子圖標題
    plt.tight_layout()  # 自動調整子圖間距

# 添加整體標題
plt.suptitle('Box Plots', fontsize=16, y=1.02)
plt.show()

# 設置畫布和子圖大小
plt.figure(figsize=(12, 10))

# 計算欄位數量
num_columns = len(data.columns)

# 繪製每個欄位的分布圖
for i, column in enumerate(data.columns, 1):  # enumerate 從 1 開始
    plt.subplot((num_columns // 3) + 1, 3, i)  # 動態計算行和列的佈局
    sns.histplot(data[column], kde=True, bins=20)  # 繪製直方圖 + KDE
    plt.title(f'Distribution of {column}')  # 每個子圖的標題
    plt.tight_layout()  # 自動調整避免重疊

# 顯示圖表
plt.suptitle('Distributions', fontsize=16, y=1.02)  # 整體標題
plt.show()

# convert all column names to lowercase except for the first column "ID"
data.columns = [col.lower() if idx != 0 else col for idx, col in enumerate(data.columns)]
test_data.columns = [col.lower() if idx != 0 else col for idx, col in enumerate(test_data.columns)]

# extract target labels
y = data.pop('medv')
features = ['indus', 'nox', 'rm', 'age', 'dis', 'tax', 'ptratio', 'lstat']
x = data[features]

# check and remove outliers from the training set (using the Z-score method)
z_scores = np.abs(stats.zscore(x))
x = x[(z_scores < 3).all(axis=1)]
y = y[x.index]

# apply log transformation to specific features to remove skewness
log_features = ['nox', 'age', 'dis', 'ptratio', 'lstat']
x[log_features] = np.log1p(x[log_features])

# standardize the features
scaler = StandardScaler()
x = scaler.fit_transform(x)

"""# Model Selection"""

models = [
    {
        'name': 'AdaBoost',
        'model': AdaBoostRegressor(estimator=tree.DecisionTreeRegressor()),
        'params':{
            'n_estimators': [50, 100, 200, 400, 600],
            'learning_rate': [0.1, 0.5, 1.0, 2.0],
            'estimator__max_depth': [3, 5, 7, 10, 15],
            'estimator__min_samples_leaf': [3, 5, 10, 15]
        }
    },
    {
       'name': 'GradiantBoosting',
        'model': GradientBoostingRegressor(),
        'params':{
            'n_estimators': [10, 50, 100, 200, 250, 300],
            'learning_rate': [0.01, 0.1, 0.5],
            'max_depth': [3, 5, 7, 10],
            'min_samples_leaf': [1, 2, 3, 5, 10, 15]
        }
    },
    {
        'name': 'CatBoost',
        'model': CatBoostRegressor(),
        'params':{
            'iterations': [100, 200],
            'learning_rate': [0.01, 0.1, 0.2, 0.5, 1],
            'depth': [4, 6, 8, 10, 16],
        }
    }
]

best_models = {}
predictions = []
actual_errors = []

"""# Training"""

for model_info in models:
    if model_info['name'] is 'CatBoost':
        print(f"Training {model_info['name']}...")
        kf = KFold(n_splits=10, shuffle=True, random_state=10)

        # find the best parameter
        grid_search = GridSearchCV(model_info['model'], param_grid=model_info['params'], cv=kf,
                                scoring='neg_mean_squared_error', return_train_score=True)
        grid_search.fit(x, y)

        best_params = grid_search.best_params_
        best_model = grid_search.best_estimator_
        print(f"Best Parameters for {model_info['name']}: {best_params}")

        results = grid_search.cv_results_
        all_rmse = []
        for mean_score, params in zip(results['mean_test_score'], results['params']):
            mean_rmse = np.sqrt(-mean_score)
            all_rmse.append((params, mean_rmse))
            print(f"Params: {params}, Mean RMSE: {mean_rmse:.4f}")

        best_rmse = min(all_rmse, key=lambda x:x[1])
        print(f"Best Params for {model_info['name']}: {best_rmse[0]}, Best Mean RMSE: {best_rmse[1]:.4f}")

        best_models[model_info['name']] = best_model

        best_model.fit(x, y)
        x_train_pred = best_model.predict(x)
        final_rmse = mean_squared_error (y, x_train_pred) ** 0.5
        print (f"Final Training RMSE for {model_info['name']}: {final_rmse}")

        # collect actual errors for ensemble
        errors = y - x_train_pred
        actual_errors.extend(errors)

        # collect predictions for ensemble
        test_data_ids = test_data['ID']
        x_test = test_data[features]
        x_test[log_features] = np.log1p(x_test[log_features])
        x_test = scaler.transform(x_test)
        y_test_pred = best_model.predict(x_test)
        predictions.append(y_test_pred)

        # save individual model predictions
        out_file(y_test_pred, test_data_ids, f"{model_info['name']}_ensemble.csv")

#compute average predictions
avg_predictions = np.mean(predictions, axis=0)

#save ensemble predictions
out_file(avg_predictions, test_data_ids, f"final_ensemble.csv")

#print average actual error
avg_actual_error = np.mean(np.abs(actual_errors))
print (f"Average Actual Error:{avg_actual_error}")