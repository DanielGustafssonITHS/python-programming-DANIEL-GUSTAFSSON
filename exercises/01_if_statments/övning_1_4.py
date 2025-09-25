kg = float(input("Vad är din vikt? "))            
age = float(input("Hur gammal är du? "))

# Viktiga här är att sätta vikten först då det enligt beskrivningen är vikten som är det som avgör mest. 
# Vikten kommer att köras först och om den inte faller inom intervallet kommer åldern inte köras alls utan ignoreras.

if 15 <= kg <= 25 and 3 <= age <= 7:
    print("Du ska ta 0.5 piller om dagen.")

elif 26 <= kg <= 40 and 7 <= age <= 12:
    print("Du ska ta 0.5-1 piller om dagen.")

elif kg > 40 and age > 12:
    print("Du ska ta 1-2 piller om dagen.")

else:
    print("Rådfråga din läkare om doseringen.")        
