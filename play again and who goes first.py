#Randomly chooses who goes first
from random import randint as randi
def firstPlayer():
    if random.randi(0,1)==0:
        return 'Computer goes first'
    else:
        return 'Player goes first'
#play again option
def playAgain():
    print ('Would the player like to play another game? (y or n)')
    return input().lower().find(y)
