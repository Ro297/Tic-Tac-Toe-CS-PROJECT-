#Drawing the board for the tic tac toe game.
def drawTTTBoard(pos):
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

drawTTTBoard([' ','0','X','X','0',' ',' ',' ',' ',' ']) 
