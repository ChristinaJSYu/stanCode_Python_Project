"""
File: weather_master.py
Name: Christina
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""


EXIT = -100


def main():
	"""
	You will address the data of weather.
	"""
	print("StanCode \"Weather Master 4.0!\"")
	temp = int(input("Next Temperature: (or -100 to quit)? "))
	cold_day = 0   # count when temperatures are below 16 degrees
	if temp == EXIT:
		print("No temperatures were entered.")
	else:
		maximum = temp
		minimum = temp
		sum_count = temp   # record the sum of all input temperatures
		times = 1   # record the number of times of input
		if temp < 16:
			cold_day += 1
		while True:
			temp = int(input("Next Temperature: (or -100 to quit)? "))
			if temp == EXIT:
				break
			else:
				if temp > maximum:
					maximum = temp
				if temp < minimum:
					minimum = temp
				if temp < 16:
					cold_day += 1
				times += 1
				sum_count += temp
		average = sum_count / times
		print("Highest Temperature = " + str(maximum))
		print("Lowest Temperature = " + str(minimum))
		print("Average = " + str(average))
		print(str(cold_day) + " cold day(s)")


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
