n = int(input("Ange ett tal: "))


fakultet = 1


for i in range(1, n + 1):
    fakultet *= i   


print(f"{n}! = {fakultet}")
