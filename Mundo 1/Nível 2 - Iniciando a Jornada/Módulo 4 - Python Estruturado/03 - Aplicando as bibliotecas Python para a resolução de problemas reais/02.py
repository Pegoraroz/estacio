import matplotlib.pyplot as plt
import numpy as np

x = ["A", "B", "C", "D"]
y = [3, 8 , 1 , 10]	

xpontos = np.array(x)
ypontos = np.array(y)

plt.bar(xpontos, ypontos)
plt.show()