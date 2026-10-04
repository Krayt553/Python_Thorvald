import math
from math import sin,cos,tan
import numpy as np


def ball_trajectory(radius):
    xValue = 0 
    yValue = 0 
    zValue = 0 

    positionStorage = []
    positionValue = 0 

    v = 0

    while v < 359: 
        positionStorage.append(positionValue)

        xValue += radius * sin(math.radians(v))
        yValue += radius * cos(math.radians(v))
        zValue += radius * tan(math.radians(v))

        positionValue = np.array[xValue, yValue, zValue]

        v += 2

    return(positionStorage)

positionStorage = ball_trajectory(10)

print(positionStorage)