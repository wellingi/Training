from random import randint
import os
import time

#Win Totals
pw=0
cw=0
ties=0

#Welcome Text
print """
Welcome to Rock, Paper, Scissors!
"""
#Rock, Paper, Scissors Script
def rps():
    print ""
    #stating globals
    global pw
    global cw
    global ties

    #Guesses
    playerguess=raw_input("Please enter Rock, Paper, or Scissors: ")
    computerguess=randint(1,3)
    #rock=1 paper=2 scissors=3
    pg=playerguess
    cg=computerguess
    print"Computer is guessing"
    time.sleep(2)

    #printing computer guess
    if computerguess==1:
        print "Computer Guessed Rock!"
    elif computerguess==2:
        print "Computer Guessed Paper"
    else:
        print "Computer Guessed Scissors"

    #determine winner
    if (pg.lower()=='rock' and cg==1) or (pg.lower()=='paper' and cg==2) or (pg.lower()=='scissors' and cg==3):
        print ""
        ties=+1
        print "Its a tie!"
        print ""
        time.sleep(1)
        print"Would you like to play again?"
        answer=raw_input("Yes or no?")
        if answer.lower()=="yes":
            os.system('clear')
            rps()
        else:
            print "Thanks for Playing!"
            print "Wins: ", pw
            print "Loses: ", cw
            print "Ties: ", ties
    elif (pg.lower()=='rock' and cg==2) or (pg.lower()=='paper' and cg==1) or (pg.lower=='scissors' and cg==2):
        print ""
        pw=+1
        print "You WIN!"
        print ""
        time.sleep(1)
        print"Would you like to play again?"
        answer=raw_input("Yes or no?")
        if answer.lower()=="yes":
            os.system('clear')
            rps()
        else:
            print "Thanks for Playing!"
            print "Wins: ", pw
            print "Loses: ", cw
            print "Ties: ", ties
    else:
        print ""
        cw=+1
        print "You LOSE!"
        print ""
        time.sleep(1)
        print"Would you like to play again?"
        answer=raw_input("Yes or no?")
        if answer.lower()=="yes":
            os.system('clear')
            rps()
        else:
            print "Thanks for Playing!"
            print "Wins: ", pw
            print "Loses: ", cw
            print "Ties: ", ties


rps()