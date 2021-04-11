#! /usr/bin/env python3

import functions as f

def main():
	temp = f.getDataFromCSV()
	x = f.normilizeData(temp[:, 0])
	y = f.normilizeData(temp[:, 1])
	print(temp[:, 0])
	print(temp[:, 1])
	theta0 = 0
	theta1 = 0
	lr = 0.01

	while True:
		tmp_theta0 = f.calcTheta0(theta0, theta1, x, y, lr)
		tmp_theta1 = f.calcTheta1(theta0, theta1, x, y, lr)
		print(theta0)
		print(theta1)
		prev_th0 = theta0
		prev_th1 = theta1
		theta0 -= tmp_theta0
		theta1 -= tmp_theta1
		if (prev_th0 - tmp_theta0 == theta0 - tmp_theta0 and prev_th1 - tmp_theta1 == theta1 - tmp_theta1):
		 	theta0, theta1 = f.restoreTheta(prev_th0, prev_th1, temp[:, 1], temp[:, 0])
		 	f.writeResult(theta0, theta1)
		 	print("done")
		 	break
		

if __name__ == "__main__":
	main()