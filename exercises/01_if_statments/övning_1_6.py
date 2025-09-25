kg = float(input("Ange vikten på din resväska: "))
width = float(input("Hur bred är din väska? "))
height = float(input("Hur hög är din väska? "))
length = float(input("Hur lång är din väska? "))

if kg > 8 or width > 40 or height > 23 or length > 55:
    print("Din väska är inte inom måtten.")
else:
    print("Din väska är godkänd.")