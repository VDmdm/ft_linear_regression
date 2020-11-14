import numpy as np

def getDataFromCSV():
	temp = np.genfromtxt("data.csv", delimiter=',')
	temp = np.delete(temp, 0, 0)
	return temp

def read_variable():
	with open('result', 'r') as f:
		lines = [float(line.rstrip()) for line in f]
	return lines

vars = read_variable()
temp = getDataFromCSV()
x = temp[:, 0]
print(vars[0])
melliage = input('Enter melliage:')
melliage = (float(melliage) - x.min()) / (x.max() - x.min())
print("Price: " + str(vars[0] + (vars[1] * melliage)))