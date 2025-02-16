import random,sys
print("Rock, Paper, Scissor")
# these variables will keep the track of wins, loses, and ties
wins=0
losses=0
ties=0
# the main game loop
while True:
    print("%swins, %s losses,%s ties"%(wins,losses,ties))
    while True:
        print("Enter your movie: (r)ock (p)aper (s)cissors or (q)uit")
        playermove=input()
        if playermove=="q":
            sys.exit()
        if playermove=="r" or playermove=="p" or playermove=="s":
            break
        print("Type of the r, p, s, or q.")
# Display what the player chooses
    if playermove== "r":
        print("ROCK versus.....")
    elif playermove== "p":
        print("PAPER versus.....")
    elif playermove== "s":
        print("SCISSOR versus.....")
# Display what the computer chooses
    randomnumber= random.randint(1,3)
    if randomnumber== 1:
        computerMove="r"
        print("ROCK")
    elif randomnumber==2:
        computerMove= "p"
        print("PAPER")
    elif randomnumber==3:
        computerMove= "s"
        print("SCISSOR")
# Display and record the win/loss/tie:
    if playermove==computerMove:
        print("It's a tie!")
        ties+=1
    elif playermove== "r" and computerMove== "s":
        print("You win!")
        wins+=1
    elif playermove== "P" and computerMove== "r":
        print("You win!")
        wins+=1
    elif playermove== "s" and computerMove== "p":
        print("You win!")
        wins+=1
    elif playermove== "r" and computerMove== "p":
        print("You Loose!")
        losses+=1
    elif playermove== "p" and computerMove== "s":
        print("You Loose!")
        losses+=1
    elif playermove== "s" and computerMove== "r":
        print("You Loose!")
        losses+=1
    
    



    