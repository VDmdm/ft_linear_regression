#! /usr/bin/env python3

import functions as f
import numpy as np
import matplotlib.pyplot as plt

def main():
	temp = f.getDataFromCSV()
	x = f.normilizeData(temp[:, 0])
	y = f.normilizeData(temp[:, 1])
	y_mean = np.mean(y)
	theta0 = 0
	theta1 = 0
	lr = 0.01
	# generate axes object
	ax = plt.axes()

	# set limits
	plt.xlim(x.min(), x.max())
	plt.ylim(y.min(), y.max())
	ax.scatter(x, y, marker='.', color='r')
	while True:
		fi_y = f.calc_fi(theta0, theta1, x)
		r2 = f.calc_accuracy(fi_y, y_mean, y)
		tmp_theta0 = f.calcTheta0(fi_y, y, lr)
		tmp_theta1 = f.calcTheta1(fi_y, x, y, lr)
		ax.set_title('accuracy: {}'.format(int(r2 * 100)))
		ln, = ax.plot(x, theta1 * x + theta0, color="black")
		print(r2 * 100)
		if (round(y_mean - np.mean(fi_y), 4) < 0.0001):
		 	theta0, theta1 = f.restoreTheta(theta0, theta1, temp[:, 1], temp[:, 0])
		 	f.writeResult(theta0, theta1)
		 	print("done")
		 	break
		theta0 -= tmp_theta0
		theta1 -= tmp_theta1
		plt.draw()
		plt.pause(0.0000001)
		ln.remove()


if __name__ == "__main__":
	main()