number = int(input("Ange ett nummer: "))

if number % 2 == 0:
    print("Numret är jämnt.")
else:
    print("Numret är ojämnt.")

if number % 5 == 0:
    print("Numret kan delas med 5.")
else:
    print("Numret kan inte delas med 5.")

if number % 2 != 0 and number % 5 == 0:
    print("Numret är ojämnt och kan delas med 5")