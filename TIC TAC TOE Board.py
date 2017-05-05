#Drawing the board for the tic tac toe game.
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
