import math

chessboard = 8 * 8
rice = 1

for i in range(1, chessboard + 1):
    rice *= 2
    if i == chessboard:
        print(f"Det finns {rice - 1} riskorn på brädet.")

