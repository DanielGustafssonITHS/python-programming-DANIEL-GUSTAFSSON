import math

p1 = (2, 1, 4)    # x1, y1, z1
p2 = (3, 1, 0)    # x2, y2, z2

# formeln är: d = roten ur (x2-x1)^2 + (y2-y1)^2 + (z2-z1)^2 

distance = math.sqrt(((((p2[0] - p1[0]) ** 2 )) + ((p2[1] - p1[1]) ** 2 )) + ((p2[2] - p1[2]) ** 2 ))

print(f"Längden mellan punkterna är {distance:.2f} l.e.")