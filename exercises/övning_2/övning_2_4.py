# randomize x and why from 1 to 10
# create variable x and assign it random value 1-10
# create variable y and assign it random value 1-10
import random

x = random.randint(1, 10)
y = random.randint(1, 10)
correct_answer = x * y

print("MatematikSpelet, där du ska visa vad du kan när det kommer till multiplikation")



# ask user x * y
# Promt, what is x * y
user_answer = int(input(f"Ditt tal är {x} * {y}, vad är ditt svar: "))




#was answer correct or not?
# use if statement for right or wrong
if user_answer == x * y:
    print("Korrekt, bra jobbat!")

elif user_answer != x * y:
    print("Du hade fel, sopa.")    


# if correct, print compliment, if incorrect tell it was wrong and write the correct number.



#Ask if the player wants to play again

#if no, end game, if yes. loop back to start again.
