word = "Ordet"
print(len(word))
uppercase_count = sum(1 for c in word if c.isupper())
lowercase_count = sum(1 for c in word if c.islower())

print("Number of uppercase letters:", uppercase_count)
print("Number of lowercase letters:", lowercase_count)
