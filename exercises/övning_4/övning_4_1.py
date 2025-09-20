# Övning A
 
import random

roll_list = []

for i in range(1, 11):
    roll_list.append(random.randint(1, 6))

roll_list.sort()
print(roll_list)

# Övning B

roll_list.sort(reverse=True)
print(roll_list)

# Övning C
print("Lägsta nummer:", min(roll_list))
print("Högsta nummer:", max(roll_list))
