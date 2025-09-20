import random

slump_num = random.randint(1000, 10000)

for i in range(slump_num + 1):
    if i == slump_num:
        print(f"The random number is {slump_num}")

