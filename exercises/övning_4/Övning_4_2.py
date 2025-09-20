dishes = ["Vegetarisk lasagne", "Spaghetti", "Fisk", "Grönsakssoppa", "Pannkakor"]
weekdays = ["Måndag", "Tisdag", "Onsdag", "Torsdag", "Fredag"]
combined = list(zip(weekdays, dishes))
print(f"Bambameny:")
for day, dish in combined:
    print(f'{day}: {dish}')
    