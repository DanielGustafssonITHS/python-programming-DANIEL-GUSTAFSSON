# input word 
word = input("Enter a word:")

# make it case-INsensitive
word = word.lower()

# check word against it's reverse
if word == word[::-1]:
    print(word, "is a palindrome")
else:
    print(word, "is not a palindrome")