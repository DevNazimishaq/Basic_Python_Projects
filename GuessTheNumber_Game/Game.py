# GuessTheGame using import module function
import random
SecretNumber=random.randint(1,20)
print("I am thinking of a number: ")

for GuessTaken in range(1,4):
    print("Take a guess: ")
    Guess=int(input())
    if Guess>SecretNumber:
        print("You guessed your number little high,")
    elif Guess<SecretNumber:
        print("Your guess is little low,")
    else:
        break
if Guess==SecretNumber:
    print("Great! you guessed my number in "+ str (SecretNumber)+"\nyou are indeed a master")
else:
    print("Nope! you need focus, the number i was thinking of was: "+ str(SecretNumber)+"")

