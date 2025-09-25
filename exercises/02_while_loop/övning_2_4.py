import random


score = 0
play_again = "ja"

# Mellan välkomsttext och loopen ska svårighetsgrad frågas om.

print("MatematikSpelet, där du ska visa vad du kan när det kommer till multiplikation")
difficulty = input("Vilken svårighetsgrad vill du ha? Lätt eller Svårt? ").lower()

if difficulty == "lätt":

    while play_again == "ja":

        x = random.randint(1, 10)
        y = random.randint(1, 10)
        correct_answer = x * y

        correct_answer = input(f"Vad är {x} x {y}? ")

        if int(correct_answer) == x*y:
            print("Rätt svar, bra jobbat!")

            score += 1

        else:
            print(f"Fel, rätt svar var {correct_answer}")

        play_again = input("Vill du spela igen? Ja eller Nej? ").lower()
           
        

    print(f"Tack för att du har spelat! Din poäng blev {score}")

else:

    while play_again == "ja":

        z = random.randint(10, 100)
        v = random.randint(10, 100)
        correct_answer = z * v

        correct_answer = input(f"Vad är {z} x {v}? ")

        if int(correct_answer) == z*v:
            print("Rätt svar, bra jobbat!")

            score += 1

        else:
            print(f"Fel, rätt svar var {correct_answer}")

        play_again = input("Vill du spela igen? Ja eller Nej? ").lower()
           
        

        print(f"Tack för att du har spelat! Din poäng blev {score}")
