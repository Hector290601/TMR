import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('detected.csv', delimiter=',', names=['direction', 'leftFitAverage', 'rightFitAverage', 'leftLine', 'rigthLine', 'time', 'lX1', 'lY1', 'lX2', 'lY2', 'rX1', 'rY1', 'rX2', 'rY2'])
#data = pd.read_csv('detected.csv', delimiter=',')
print(data)

data.drop([1], axis = 0)

lX1 = data['lX1']
lY1 = data['lY1']
lX2 = data['lX2']
lY2 = data['lY2']
rX1 = data['rX1']
rY1 = data['rY1']
rX2 = data['rX2']
rY2 = data['rY2']

lX1Array = lX1.to_numpy()
lY1Array = lY1.to_numpy()
lX2Array = lX2.to_numpy()
lY2Array = lY2.to_numpy()

rX1Array = rX1.to_numpy()
rY1Array = rY1.to_numpy()
rX2Array = rX2.to_numpy()
rY2Array = rY2.to_numpy()
"""
plt.plot(lX1Array, lY1Array, 'r')
plt.plot(rX1Array, rY1Array, 'g')
plt.plot(lX2Array, lY2Array, 'r--')
plt.plot(rX2Array, rY2Array, 'g--')
"""

plt.plot(lY1Array, lX1Array, 'r')
plt.plot(rY1Array, rX1Array, 'g')
plt.plot(lY2Array, lX2Array, 'r--')
plt.plot(rY2Array, rX2Array, 'g--')

plt.show()
