import matplotlib.pyplot as plt
import numpy as np

#x =  [i for i in range(11)]
x = np.linspace(0, 10) #cria uma lista de valores segmentados em 50 partes de 0 a 10

def power_2(a):
    return a ** 2
def power_3(a):
    return a ** 3

y1 = [power_2(y) for y in x]
y2 = [power_3(y) for y in x]

print(x)
print(y2)
plt.plot(x, x, label="linear")
plt.plot(x, y1, label="square")
plt.plot(x, y2, label="cubic")
plt.axis([0, 11, 0, 11])
plt.axes().set_aspect('equal')
plt.yticks([tick for tick in range(0, 11)])
plt.xticks([tick for tick in range(0, 11)])
plt.show()