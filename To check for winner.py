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
