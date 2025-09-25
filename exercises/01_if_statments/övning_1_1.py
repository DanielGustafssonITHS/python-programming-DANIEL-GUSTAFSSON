number = float(input("Ange ett tal: "))       #input kräver att man anger ett nummer

# Här frågas om number är mindre än noll, större än noll eller noll. Beroende på nummer så printas det svaret.

if number < 0:
    print("Ditt tal är negativt.")

elif number > 0:
    print("Ditt tal är positivt.")

else:
    print("Ditt tal är noll.")