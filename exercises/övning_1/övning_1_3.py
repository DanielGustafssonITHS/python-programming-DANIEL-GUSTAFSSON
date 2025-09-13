angle1 = float(input("Här ska vi se om din triangel är rätvinklig.\nAnge första vinkeln: "))
angle2 = float(input("Ange andra vinkeln: "))
angle3 = float(input("Ange tredje vinkeln: "))

# Då vinkelarna i en triangel inte kan vara negativa eller 0 så frågar jag först om vinklarna som är angivna är större än 0
# och att dom tillsammans blir 180 grader.

if angle1 > 0 and angle2 > 0 and angle3 > 0 and (angle1 + angle2 + angle3 == 180):

# Här frågar jag om nån av de 3 vinklarna uppfyller kravet på 90 grader.
    
    if angle1 == 90 or angle2 == 90 or angle3 == 90:
        print("Detta är en rätvinklig triangel.")

    else:
        print("Detta är inte en rätvinklig triangel.")

# Detta är ifall inget av det andra stämmer och då inte är en triangel.

else:
    print("Detta är inte en triangel, vinklarna i en triangel måste bli 180 grader tillsammans!")  