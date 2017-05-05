#Code for Tic Tac Toe by Rohan Poddar, Rohan Sahni and Ashna Kedia
#Taken help from http://inventwithpython.com/chapter10.html
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
        print ('What is your move? (1-9)')
        move = input()
        print 'Invalid Move'
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
            
print 'In a galaxy far far away, humans and machines are fighting to secure dominance over the other. The machines have challenged the humans to a game of Tic Tac Toe to see who gains control of the galaxy'
name = raw_input("Who is representing the humans for their survival? ")
print 'Hello ' + name +',puny human.' + 'I am Pokul Grabhu, champion of the machines. I challenge you to beat me and take control of the galaxy!'
position = [' ']*9
usercounter = ''
while usercounter != 'X' and usercounter != 'O':
    print ('Choose counter: X or O')
    usercounter = str(raw_input())
    usercounter = usercounter.upper()
if usercounter == 'X':
    computercounter = 'O'
    print 'The Humans have chosen X, The machines are O'
else:
    computercounter = 'X'
    print 'The Humans have chosen O, The machines are X'
player1 = goes_first()
if player1 == 'User':
   print 'Make your move puny human!'
else:
    print 'Hail the Machines! We make the first move.'
gameover = False
while True:
    while gameover == False:
        if player1 == 'User':
            move = user_move()
            make_move(position,usercounter,move)
            drawTTTboard(position)
            if check4win(position,usercounter):
                print 'YOU WIN! looks like you are not so puny after all! The Machines will be back soon!!'
                gameover = True
            elif check4full(position):
                drawTTTboard(position) 
                print 'DRAW! Humans and Machines will fight forever!'
                gameover = True
            else:
                player1 = 'Computer'        
        else:
            emptyspaces = []
            for i in range(0,9):
                if freespace(position,i) == True:
                    emptyspaces.append(i)
            computermove = random.choice(emptyspaces)
            make_move(position,computercounter,computermove)
            print 'I have made my move!'
            drawTTTboard(position)
            if check4win(position,computercounter):
                    print 'YOU LOSE! The machines have taken over. Bow down to your kings, Puny Human!'
                    gameover = True 
            elif check4full(position):
                drawTTTboard(position)
                print 'DRAW! Humans and Machines will fight forever!'
                gameover = True
            else:
                player1 = 'User'

    if gameover == True:
        print 'Do you want to play again? (Yes or No)?'
        response=raw_input().lower()
        decision=response.count('y')
        if decision>=1:
            gameover = False
            position = [' ']*9
        else:
            break
        
    
        
            
                           
