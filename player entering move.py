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
