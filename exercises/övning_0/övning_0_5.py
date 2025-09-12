import math

p1 = (3, 5)        # x1 = 3    y1 = 5
p2 = (-2, 4)       # x2 = -2   y2 = 4
distance = math.sqrt(((p1[0] - p2[0]) ** 2) + ((p1[1] - p2[1]) ** 2))
print(f"Distansen mellan punkterna är {distance:.1f} längdenheter")
