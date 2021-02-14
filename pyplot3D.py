from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = plt.axes(projection = '3d')

x = np.linspace(-4,4,100)
y = np.linspace(-4,4,100)

x, y = np.meshgrid(x, y)

z = 1 - 2*x + 3*y

ax.contour3D(x, y, z, 50)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

plt.show()