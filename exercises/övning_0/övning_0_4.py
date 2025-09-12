a = (4, 4)  # Första punkten: x1=4, y1=4
b = (0, 1)  # Andra punkten: x2=0, y2=1

k = (b[1] - a[1]) / (b[0] - a [0])  # (y2-y1) / x2-x1 = k
m = a[1] - k * a[0]   # m = y1 - k * x1       m = 4 - 0.75 * 4      m = 1

print(f"Lutningen k är {k}")
print(f"Skärningen med y-axeln m är {m}")
print(f"Ekvationen är: y = {k}x + {m}")

