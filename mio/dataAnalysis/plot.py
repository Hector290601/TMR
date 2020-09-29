import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('detected.csv', delimiter=',', names=['direction', 'leftFitAverage', 'rightFitAverage', 'leftLine', 'rigthLine', 'lX1', 'lY1', 'rX1', 'rY1'])

#data.drop([1], axis = 0)

lX1 = data['lX1']
lX2 = data['lY1']
rX1 = data['rX1']
rX2 = data['rY1']

lX1Array = lX1.to_numpy()
lY1 = range(len(lX1Array))

rX1Array = rX1.to_numpy()
rY1 = range(len(rX1Array))

lX2Array = lX2.to_numpy()
lY2 = range(len(lX2Array))

rX2Array = rX2.to_numpy()
rY2 = range(len(rX2Array))

#plt.plot(lX1Array, lY1, 'r')
#plt.plot(rX1Array, rY1, 'g')
plt.plot(lX2Array, lY2, 'b')
plt.plot(rX2Array, rY2, 'm')

plt.show()
