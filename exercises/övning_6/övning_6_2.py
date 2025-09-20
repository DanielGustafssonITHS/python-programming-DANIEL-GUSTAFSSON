# Övning A & B

import math

def Euclidean_dist(p1, p2, q1, q2):
    euclid_dist = math.sqrt((p1 - q1)**2 + (p2 - q2)**2)
    return euclid_dist

p1 = float(input("Input p1: "))
p2 = float(input("Input p2: "))
q1 = float(input("Input q1: "))
q2 = float(input("Input q2: "))

dist = Euclidean_dist(p1, p2, q1, q2)
print(f"The distance is {dist:.1f}")




# Övning C


origin = (0, 0)
points = [(10, 3), (-1, -9), (10, -10), (4, -2), (9, -10)]

for point in points:
    distance = Euclidean_dist(origin[0], origin[1], point[0], point[1])
    print(f"Distance from {origin} to {point} is {distance:.1f}")