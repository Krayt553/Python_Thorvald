import numpy as np

positionA = np.array([1, 0, 0])
positionB = np.array([5, 0, 1])
positionC = np.array([67, 0, 0])
massA = 2
massB = 2
massC = 5

#Positions are vectors, masses are integers
def calculate_center_of_mass_coordinates(a, b, c):
    numerator = a * massA + b * massB + c * massC
    denominator = massA + massB + massC
    return numerator / denominator

def calculate_center_of_mass(positionA, positionB, positionC, massA, massB, massC):
    x = calculate_center_of_mass_coordinates(positionA[0], positionB[0], positionC[0])
    y = calculate_center_of_mass_coordinates(positionA[1], positionB[1], positionC[1])
    z = calculate_center_of_mass_coordinates(positionA[2], positionB[2], positionC[2])

    return np.array([x,y,z])

centerMass = calculate_center_of_mass(positionA, positionB, positionC, massA, massB, massC)

print(centerMass)

    








