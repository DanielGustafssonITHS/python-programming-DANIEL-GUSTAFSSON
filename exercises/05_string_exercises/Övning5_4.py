# Räkna antalet vokaler (emgelska vokaler) i en mening

def countvowels(string):
    num_vowels = 0
    for char in string:
        if char in "aeiouAEIOU":
           num_vowels = num_vowels+1
    return num_vowels


text = input("Enter a sentence: ")
print("Number of vowels:", countvowels(text))