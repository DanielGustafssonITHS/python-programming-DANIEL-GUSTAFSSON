# Alternativ 1

import random                                                         # importerar random så att man kan använda slumpmässiga tal.

correct_number = random.randint(1, 100)                               # Väljer ett random nummer mellan 1 och 100

guess = None                                                          # För att ge variabeln ett värde sätter vi den på None då vi inte gissat än

while guess != correct_number:                                        # Fortsätt gissa tills det blir rätt
    guess = int(input("Välj ett nummer mellan 1 och 100: "))          # Ger guess varibeln ett värde

    if guess < correct_number:                                        # Om gissningen är lägre än svara så säger den det och du ska ge en ny högre gissning
        print("Du gissade för lågt, gissa högre.")

    elif guess > correct_number:                                      # Samma som ovan fast tvärtom
        print("Du gissade för högt, gissa lägre.")    

    else:                                                             # Gissar du rätt får du det svaret och spelet avslutas.
        print("Korrekt gissing, bra jobbat!") 