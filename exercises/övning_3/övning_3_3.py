# Övning 1A 

for i in range(0, 11):
    print(f"6 x {i} = {6 * i}")
    


# Övning 1B





# Vilket nummer vill du ha
tabell = int(input("Vilken gångertabell är du intresserad av? "))
# ger tabell ett värde5

start_num = int(input("Välj lägsta nummer att gångra med? "))
# ger start_num ett värde 

end_num = int(input("Vilket är sista numret du vill gångra med? "))
#ger end_num ett värde

for i in range(start_num, end_num + 1):
    print(f"{tabell} x {i} = {tabell * i}")

 
 
 
 
 # Övning 1C
 

for x in range(0, 11):
    for y in range(0,11):
        print(f"{x * y:4}", end = " ")
    print()    

