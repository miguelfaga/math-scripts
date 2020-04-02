import numpy as np
import matplotlib.pyplot as plt
from math import pi, sqrt

x = np.linspace(-1, 1, num=10000000)

def circle(x):
    return sqrt(1 - x**2)

y1 = [circle(y) for y in x]
y2 = [-circle(y) for y in x]

plt.plot(x, y1, color="blue")
plt.plot(x, y2, color="blue")
plt.axis([-1.1, 1.1, -1.1, 1.1])
plt.axes().set_aspect('equal')
plt.show()