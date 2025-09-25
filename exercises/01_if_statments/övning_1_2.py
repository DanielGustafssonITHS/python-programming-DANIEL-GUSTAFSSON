number1 = float(input("Ange ditt första tal: "))
number2 = float(input("Ange ditt andra tal: "))


# Här frågas om number2 är större än number1 och om det är det som anger den det, annars anges number1 som största talet.

if number1 < number2:
    print(f"{number2:.0f} är det största talet.")

else:
    print(f"{number1:.0f} är det största talet.")    