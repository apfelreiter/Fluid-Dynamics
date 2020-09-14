from scipy.spatial import Delaunay
import matplotlib.pyplot as plt
import numpy as np


print("Hello")


points = np.array([[0, 0], [0, 1.1], [1, 0], [1, 1]])
tri = Delaunay(points)

plt.triplot(points[:,0], points[:,1], tri.simplices)
plt.plot(points[:,0], points[:,1], 'o')

plt.show()