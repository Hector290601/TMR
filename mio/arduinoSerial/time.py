import time

startTime = time.time()

while True:
    currentTime = time.time()
    delta = currentTime - startTime
    if delta >= 1:
        startTime = time.time()
        print('ha pasado otro segundo')



