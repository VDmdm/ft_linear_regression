#! /usr/bin/env python3

import functions as f

def main():
	theta0, theta1 = f.read_variable()
	temp = f.getDataFromCSV()
	x = temp[:, 0]
	melliage = float(input('Enter melliage: '))
	# melliage = (float(melliage) - x.min()) / (x.max() - x.min())
	price = theta0 + (theta1 * melliage)
	if price <= 0 or melliage <= 0:
		print("Can't predict this")
	else:
		print("Price: " + str(round(price, 2)))

if __name__ == "__main__":
	main()