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

def normilizeData(var):
	return (var - var.min()) / (var.max() - var.min())

def estimatePrice(theta0, theta1, milleage):
	return theta0 + (theta1 * milleage)

def calcTheta0(th0, th1, x, y, lr):
	summ = 0
	for i in range(len(x) - 1):
		summ += estimatePrice(th0, th1, x[i]) - y[i]
	return lr * (summ / len(x))

def calcTheta1(th0, th1, x, y, lr):
	summ = 0
	for i in range(len(x) - 1):
		summ += (estimatePrice(th0, th1, x[i]) - y[i]) * x[i]
	return lr * (summ / len(x))

temp = getDataFromCSV()
x = normilizeData(temp[:, 0])
y = temp[:, 1]
theta0 = 0
theta1 = 0
lr = 0.1

while True:
	tmp_theta0 = calcTheta0(theta0, theta1, x, y, lr)
	tmp_theta1 = calcTheta1(theta0, theta1, x, y, lr)
	prev_th0 = theta0
	theta0 -= tmp_theta0
	theta1 -= tmp_theta1
	if (prev_th0 - tmp_theta0 == theta0 - tmp_theta0):
		writeResult(theta0, theta1)
		print("done")
		break



#plt.figure(figsize=(16, 9))
#plt.title('bla')
#plt.scatter(X, Y, s=256, color='#27ae60', alpha=0.5, label='Y')
#plt.plot(X, y_preds, color='#000000', linewidth=4, label='linear pred')
#plt.show()