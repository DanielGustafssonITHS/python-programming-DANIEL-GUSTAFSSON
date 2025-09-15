i = 0                         # Standard start
all_total = 0                 # Behöver en variabel att lägga summan i 
odd_total = 0

while i <= 100:               # Lägger till tills "i" är större eller lika med 100
    all_total += i            # Placerar det aktuella talet in i sum_total
    
    if i % 2 == 1:            # Placerar udda tal i odd_total
        odd_total += i        # Placerar det aktuella talet i odd_total.
        
                      
    i += 1                    # Ökar värdet på i med 1 varje loop 1+2+3+4+5 osv till 100. I andra summan ökar den värdet varannan loop.

print(f"Den totala summan av 0-100 är {all_total}.")    
print(f"Den totala summan av udda tal är {odd_total}.")