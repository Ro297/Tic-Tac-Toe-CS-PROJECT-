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
    move = choosefromList(board,[1,3,7,9])
    if move != None:
        return move
    if freeSpace(board,5):
        return 5

    return choosefromList(board,[2,4,6,8])


                
