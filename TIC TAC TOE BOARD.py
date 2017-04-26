import random

#Drawing the board for the tic tac toe game.
def drawBoard(board):
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
#We are ignoring the 0th index in order to avoid confusion. So code shouldn't fill anything in the 0th place.

drawBoard([' ','0','X','X','0',' ',' ',' ',' ',' ']) 
