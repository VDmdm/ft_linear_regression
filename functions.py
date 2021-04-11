import numpy as np
import matplotlib.pyplot as plt

def writeResult(th0, th1):
	with open('result', 'w') as f:
		f.write(str(th0) + '\n')
		f.write(str(th1))

def getDataFromCSV():
	temp = np.genfromtxt("data.csv", delimiter=',')
	temp = np.delete(temp, 0, 0)
	return temp

def read_variable():
	with open('result', 'r') as f:
		lines = [float(line.rstrip()) for line in f]
	return lines[0], lines[1]

def normilizeData(var):
	return (var - var.min()) / (var.max() - var.min())

def restoreTheta(theta0, theta1, price, km):
	newTheta1 = (price.max() - price.min()) * theta1 / (km.max() - km.min())
	newTheta0 = price.min() + ((price.max() - price.min()) * theta0) + newTheta1 * (1 - km.min())
	return newTheta0, newTheta1

def estimatePrice(theta0, theta1, milleage):
	return theta0 + (theta1 * milleage)

def calcTheta0(th0, th1, x, y, lr):
	summ = 0
	for i in range(len(x)):
		summ += estimatePrice(th0, th1, x[i]) - y[i]
	return lr * (summ / len(x))

def calcTheta1(th0, th1, x, y, lr):
	summ = 0
	for i in range(len(y)):
		summ += (estimatePrice(th0, th1, x[i]) - y[i]) * x[i]
	return lr * (summ / len(y))

def show_plot(x, y, plt_xy, plt_xy2):
	fig = plt.figure()
	ax = fig.add_subplot(1, 1, 1)
	ax.scatter(x, y)
	ax.plot(plt_xy, plt_xy2, 'o-r')
	plt.legend()
	plt.grid(True)
	plt.show()