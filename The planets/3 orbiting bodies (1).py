import numpy as np
import math as math
import matplotlib.pyplot as plt

massA = 10
massB = 10 
massC = 5

gravConstant = 6.67e-11
solarMass = 2e30
astronomicalUnit = 1.5e11
kilometer = 1e+10
timeStep = 0.1

class object:
    def __init__(self, mass, position, velocity):
        self.mass = float(mass * solarMass)
        self.position = np.array([float(x * kilometer) for x in position])
        self.velocity = np.array([float(x) for x in velocity])

objectA = object(2.9, [100, 0, 0], [2, 13, 40])
objectB = object(2.9, [0, 100, 0], [2, 13, 40])
objectC = object(2.9, [0, 0, 100], [2, 13, 40])

def calculate_grav_force(centralMass, orbitingMass, relativeDistance):   
    return ((gravConstant * centralMass * orbitingMass) / (relativeDistance * relativeDistance))

def calculate_relative_distance(object1, object2):
    xDif = object1.position[0] - object2.position[0]
    yDif = object1.position[1] - object2.position[1]
    zDif = object1.position[2] - object2.position[2]

    return (math.sqrt(xDif * xDif + yDif * yDif + zDif * zDif))

def calculate_direction_vector(object1, object2):
    xDif = object2.position[0] - object1.position[0]
    yDif = object2.position[1] - object1.position[1]
    zDif = object2.position[2] - object1.position[2]

    vector12 = [xDif, yDif, zDif]
    length = math.sqrt(xDif * xDif + yDif * yDif + zDif * zDif)

    return np.array([x / length for x in vector12])

def update_interbody_forces(object1, object2):
    forceBetween = calculate_grav_force(object1.mass, object2.mass, calculate_relative_distance(object1, object2))
    directionBetween = calculate_direction_vector(object1, object2)

    return np.array([direction * forceBetween for direction in directionBetween])
    
def update_objects_force(objectA, objectB, objectC):
    forceAB = update_interbody_forces(objectA, objectB)
    forceAC = update_interbody_forces(objectA, objectC)

    forceBA = update_interbody_forces(objectB, objectA)
    forceBC = update_interbody_forces(objectB, objectC)

    forceCA = update_interbody_forces(objectC, objectA)
    forceCB = update_interbody_forces(objectC, objectB)

    for i in range(3):
        forceAB[i] += forceAC[i]
        forceBA[i] += forceBC[i]
        forceCA[i] += forceCB[i]

    totalForceA = forceAB
    totalForceB = forceBA
    totalForceC = forceCA

    return (totalForceA, totalForceB, totalForceC)

def apply_force_to_velocity(objectA, objectB, objectC):

    totalForceA, totalForceB, totalForceC = update_objects_force(objectA, objectB, objectC)

    for i in range(3): 
        totalForceA[i] = totalForceA[i] / objectA.mass
        totalForceB[i] = totalForceB[i] / objectB.mass
        totalForceC[i] = totalForceC[i] / objectC.mass

    accelerationObjectA = totalForceA
    accelerationObjectB = totalForceB
    accelerationObjectC = totalForceC

    for i in range(3): 
        objectA.velocity[i] += (accelerationObjectA[i] * timeStep)
        objectB.velocity[i] += (accelerationObjectB[i] * timeStep)
        objectC.velocity[i] += (accelerationObjectC[i] * timeStep)

def move_objects(objectA, objectB, objectC): 

    apply_force_to_velocity(objectA, objectB, objectC)

    for i in range(3):
        objectA.position[i] += objectA.velocity[i]
        objectB.position[i] += objectB.velocity[i]
        objectC.position[i] += objectC.velocity[i]

def graph_v_over_time(objectA, objectB, objectC):
    objectAVelocities = []
    objectBVelocities = []
    objectCVelocities = []

    stepsPassed = []

    for x in range(int(float(10000))):
        velocityAMagnitude = 0 
        velocityBMagnitude = 0
        velocityCMagnitude = 0

        stepsPassed.append(x)

        move_objects(objectA, objectB, objectC)

        for i in range (3): 
            velocityAMagnitude += objectA.velocity[i]
            velocityBMagnitude += objectB.velocity[i]
            velocityCMagnitude += objectC.velocity[i]

        objectAVelocities.append(abs(velocityAMagnitude))
        objectBVelocities.append(abs(velocityBMagnitude))
        objectCVelocities.append(abs(velocityCMagnitude))

    plt.plot(stepsPassed, objectAVelocities)
    plt.plot(stepsPassed, objectBVelocities)
    plt.plot(stepsPassed, objectCVelocities)
    plt.xlabel("Time")
    plt.ylabel("Velocity")
    plt.title("Velocities over time")

    allVelocities = objectAVelocities + objectAVelocities + objectCVelocities
    minVelocities = min(allVelocities)
    maxVelocities = max(allVelocities)

    #plt.ylim(bottom = 10, top = 60)

    plt.show()

    print(f"Max velocity: {maxVelocities}")
    print(f"Min velocity: {minVelocities}")
    
    return (objectAVelocities, objectBVelocities, objectCVelocities)

def graph_two_objects_motion(object1, object2,objectSecondary):
    object1Positions = []
    object2Positions = []

    for i in range(int(float(10000))):

        move_objects(object1, object2, objectSecondary)

        for i in range (1):
            object1Positions.append(object1.position)
            object2Positions.append(object1.position)

    #print(f"Object 1 positions = {object1Positions}")
    #print("---"*10)
    #print(f"Object 2 positions = {object2Positions}")


graph_v_over_time(objectA, objectB, objectC)