# Alternativ 2

import random 

lowest_number = 1                                                                   # Sätter intervallet mellan 1 och 100
highest_number = 100
answer = random.randint(lowest_number, highest_number)                              # Variabeln väljer ett random nummer mellan intervallerna
guesses = 0                                                                         # Lagrar hur många gissningar det tar att få rätt svar
is_running = True                                                                   # Boolean värde som anges som True och när rätt svar givs ändras till False

print("Gissningsspelet!")
print(f"Välj ett nummer mellan {lowest_number} and {highest_number}: ")

while is_running:                                                                   # Betyder att så länge is_running är True fortsätter loopen

    guess = input("Vad är din gissning? ")

    if guess.isdigit():                                                             # Om gissningen inte är en siffra så triggas else prompten
        guess = int(guess)
        guesses += 1                                                                # Lägger till 1 i guesses för varje gissning du gör.

        if guess < lowest_number or guess > highest_number:
            print("Numret är utanför det bestämda intervallet")
            print(f"Välj ett nummer mellan {lowest_number} and {highest_number}")

        elif guess < answer:
            print("För lågt, försök igen!")

        elif guess > answer:
            print("För högt, försök igen!") 

        else:
            print(f"Bra jobbat, rätt nummer var: {answer}")
            print(f"Antalet gissningar var: {guesses}")  

            is_running = False        
    else:
        print("Ogiltlig gissning.")
        print(f"Välj ett nummer mellan {lowest_number} and {highest_number}")
