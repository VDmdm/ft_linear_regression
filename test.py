#! /usr/bin/env python3

# import functions as f
# from matplotlib import pyplot as plt

# fig = plt.figure()
# for i in range(10000):
# 	temp = f.getDataFromCSV()
# 	x = temp[:, 0]
# 	y = temp[:, 1]
# 	ax = fig.add_subplot(1, 1, 1)
# 	ax.scatter(x, y)
# 	ax.plot([100000 + i, 5000 + i], [20000, 100000])
# 	plt.legend("bla")
# 	plt.grid(True)
# 	plt.draw()

import functions as f
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
plt.style.use('seaborn-pastel')
 
temp = f.getDataFromCSV()
x = temp[:, 0]
y = temp[:, 1]
print(x)
print(y)
fig = plt.figure()
ax = plt.axes()
line, = ax.plot([], [], lw=3)
 
def init():
    line.set_data([], [])
    return line,
def animate(i):
    line.set_data(x, y)
    return line,
 
anim = FuncAnimation(fig, animate, init_func=init,
                               frames=200, interval=20, blit=True)
plt.show()