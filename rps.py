import random
import os


#clear screen
def erase():
    os.system('clear')

#gameplay
def rps():

    #What beats what
    winner = {
        "rock" : "scissors",
        "paper" : "rock",
        "scissors" : "paper",
    }

    #scores and loop
    keep_playing=True
    win=0
    lose=0
    ties=0

    while keep_playing==True:
        erase()
        playerguess=raw_input(" Please enter Rock, Paper, or Scissors: ").lower() # Players Guess
        computerguess=random.choice(["rock", "paper", "scissors"]) #Computer Guess

        erase()
        print " You guessed", playerguess
        print ""
        print " The computer guessed", computerguess
        print ""

        #Deciding who won
        if playerguess == computerguess:
            print " Its a Tie!"
            ties += 1
        elif winner[playerguess]==computerguess:
            print " You win!"
            win += 1
        else:
            print " You Lose"
            lose += 1
        print ""

        #Play again statment
        print" Would you like to play again? Yes or No?"
        answer=raw_input(" >")
        if answer == "no":
            erase()
            print " Thank you for playing! Here are your results!"
            print " Total Wins:", win
            print " Total Loses:",lose
            print " Total Ties:",ties
            keep_playing=False


#Welcome Text
print """
    Welcome to Rock, Paper, Scissors!
    ---------------------------------
    Where Rock Beats Scissors,
    Scissors Cuts Paper,
    And Paper Cuts Rock!
    ---------------------------------
    Would you like to play? Yes or No?
"""
play=raw_input(" >").lower()
if play=="yes":
    rps()
else:
    print "Oh well!"


