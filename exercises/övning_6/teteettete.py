def area_calculator(base, height):
    return (base * height) / 2

# Användaren matar in värden utanför funktionen
b = float(input("Input the base of your triangle: "))
h = float(input("Input the height of your triangle: "))

# Anropa funktionen och skriv ut resultatet
area = area_calculator(b, h)
print(f"The area of your triangle is {area}")

area_calculator(b, h) 