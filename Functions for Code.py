import random
from random import randint as randi

def drawTTTboard(position):
    print('   |'*2)
    print(' ' + position[0] + ' | ' + position[1] + ' | ' + position[2])
    print('   |'*2)
    print('-'*11)
    print('   |'*2)
    print(' ' + position[3] + ' | ' + position[4] + ' | ' + position[5])
    print('   |'*2)
    print('-'*11)
    print('   |'*2)
    print(' ' + position[6] + ' | ' + position[7] + ' | ' + position[8])
    print('   |'*2)

def goes_first():
    if randi(0,1)==1:
        return 'User'
    else:
        return 'Computer'

def user_move():
    move = ' '  
    while move not in [0,1,2,3,4,5,6,7,8] or not freespace(position,move):
        print ('What is your next move? (1-9)')
        move = input()
        return int(move-1)

def freespace(position, move):
    return position[move] == ' '

def make_move(position,counter, move):
    position[move] = counter

def check4win(position,counter):
    return ((position[0]==counter and position[1]==counter and position[2]==counter)or
            (position[3]==counter and position[4]==counter and position[5]==counter)or
            (position[6]==counter and position[7]==counter and position[8]==counter)or
            (position[0]==counter and position[3]==counter and position[6]==counter)or
            (position[1]==counter and position[4]==counter and position[7]==counter)or
            (position[2]==counter and position[5]==counter and position[8]==counter)or
            (position[0]==counter and position[4]==counter and position[8]==counter)or
            (position[2]==counter and position[4]==counter and position[6]==counter))

def check4full(position):
    for i in range (0,9):
        if freespace(position, i):
            return False
    return True
