"""
File: webcrawler.py
Name: Christina
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10900879
Female Number: 7946050
---------------------------
2000s
Male Number: 12977993
Female Number: 9209211
---------------------------
1990s
Male Number: 14146310
Female Number: 10644506
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html)
        # ----- Write your code below this line ----- #
        tags = soup.find_all("tbody")
        times = 0  # check whether it is within first 200 rank
        male_num = 0
        female_num = 0
        for tag in tags:
            tokens = tag.text.split()
            for i in range(len(tokens)):
                if times == 200:
                    break
                if i % 5 == 2:
                    male_num += int(tokens[i].replace(',', ''))
                elif i % 5 == 4:
                    female_num += int(tokens[i].replace(',', ''))
                    times += 1
        print(f"Male Number: {male_num}")
        print(f"Female Number: {female_num}")


if __name__ == '__main__':
    main()
