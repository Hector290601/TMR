import numpy as np
import matplotlib.pyplot as plt

nPts = 100
np.random.seed(0)
bias = np.ones(nPts)
topRegion = np.array([np.random.normal(10, 2, nPts), np.random.normal(12, 2, nPts), bias]).T
bottomRegion = np.array([np.random.normal(5, 2, nPts), np.random.normal(6, 2, nPts), bias]).T
allPoints = np.vstack((topRegion, bottomRegion))
w1 = -0.2
w2 = -0.35
b = 3.5
#print(allPoints)
lineParameters = np.matrix([w1, w2, bias])
x1 = bottomRegion = [:, 0].min()
#w1x1 + w2x2 +b = 0
x2 = -b / w2 + x1 * (-w1 / w2)
#print(randomX1Values)
#print(randomX2Values)
#print(topRegion)
_, ax = plt.subplots(figsize=(4, 4))
ax.scatter(topRegion[:, 0], topRegion[:, 1], color='r')
ax.scatter(bottomRegion[:, 0], bottomRegion[:, 1], color='b')
plt.show()