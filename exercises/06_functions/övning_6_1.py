def area_calculator(base, height):              # Detta är då själva funktionen
    return (base * height) / 2


b = float(input("Input the base of your triangle: "))
h = float(input("Input the height of your triangle: "))


area = area_calculator(b, h)
print(f"The area of your triangle is {area}")

area_calculator(b, h) 