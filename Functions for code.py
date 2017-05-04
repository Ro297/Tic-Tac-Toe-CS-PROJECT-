import random
from random import randint as randi

def drawTTTBoard(pos):
#Drawing the board for the tic tac toe game.
    print('   |   |')
    print(' ' + pos[1] + ' | ' + pos[2] + ' | ' + pos[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + pos[4] + ' | ' + pos[5] + ' | ' + pos[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + pos[7] + ' | ' + pos[8] + ' | ' + pos[9])
    print('   |   |')
#We are ignoring the 0th index in order to avoid confusion. So code shouldn't fill anything in the 0th place.

def PlayerCounter():
#We will use the while not function so that the program continues only when it has the value X or 0
    counter = ''
    while not (counter == 'X' or counter == 'O'):
        print ('Choose counter: X or O')
        counter = input().upper()

    if counter == 'X':
        return ['Player is X','Computer is O']
    else:
        return ['Player is O','Computer is X']

#Randomly chooses who goes first
def firstPlayer():
    if random.randi(1,2)==1:
        return 'Player goes first'
    else:
        return 'Computer goes first'

#play again option
def playAgain():
    print ('Would the player like to play another game? (y or n)')
    return input().lower().find(y)

def playerMove(board, counter, move):
    board[move]=counter

#Code to check if the game is over. We write down all the possible ways to win
def Winner(board, counter):
    return ((board[1]==counter and board[2]==counter and board[3]==counter)or
            (board[4]==counter and board[5]==counter and board[6]==counter)or
            (board[7]==counter and board[8]==counter and board[9]==counter)or
            (board[1]==counter and board[4]==counter and board[7]==counter)or
            (board[2]==counter and board[5]==counter and board[8]==counter)or
            (board[3]==counter and board[6]==counter and board[9]==counter)or
            (board[1]==counter and board[5]==counter and board[9]==counter)or
            (board[3]==counter and board[5]==counter and board[7]==counter))

def drawTTTBoardCopy():
    copyTTTBoard = []

    for i in board:
        copyTTTBoard.append(i)
    return copyTTTBoard

def freeSpace(board, move):
    return board[move]== ' '
#gives true value if space on the board is empty

def playerMove(board):
    move=' '
    while move not in '1 2 3 4 5 6 7 8 9'.split or not freeSpace(board, int(move)):
        print ('What is your next move? (1-9')
        move = input()
    return int(move)
#We use int in order to take the input as a number which we will later add to the list. 

def makeMoveList(board, list_moves):
    moves_possible= []
    for i in list_moves:
        if freeSpace(board,i):
            moves_possible.append(i)

if len(moves_possible)!=0:
    return random.choice(moves_possible)
else:
    return None



#AI for the computer to make move
def computerMove(board, computerCounter):
    if computerCounter == '0':
        counter = 'X'
    else:
        counter = '0'

    for i in range(1,10):
        copy = copyTTTBoard(board)
        if freeSpace(copy,i):
            makeMove(copy,computerCounter,i)
            if winner(copy,computerCounter):
                return i

    for i in range(1,10):
        copy = copyTTTBoard(board)
        if freeSpace(copy,i):
            makeMove(copy,counter,i)
            if winner(copy,counter)):
                return i
    move = makeMoveList(board,[1,3,7,9])
    if move != None:
        return move
    if freeSpace(board,5):
        return 5

    return choosefromList(board,[2,4,6,8])

def fullBoard(board):
    for i in range(1,10):
        if freeSpace(board,i):
            return False
        return True





                


