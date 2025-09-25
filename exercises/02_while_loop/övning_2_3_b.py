import random

low = 1                                                                                                 # Basic variabler men en randomint funktion
high = 100
correct_answer = random.randint(low, high)
guess = None
tries = 0 

while guess != correct_answer:                                                                          # Så länge gissningen är fel så heltalsdivisioneras gissningen och 
    guess = (low + high) // 2                                                                           # nästa tal blir mellan det som gissades och högsta eller lägsta        
    tries += 1                                                                                          # som är kvar, den väljer siffran i mitten varja gång helt enkelt
    print(f"Försök nr: {tries}. Datorn gissar på nr: {guess}")

    if guess < correct_answer:
        low = guess + 1

    elif guess > correct_answer:
        high = guess - 1

    else:
        print(f"Rätt nummer! Numret var {correct_answer}. Datorn gissade det på {tries} försök.")      