def user_move():
    move = ' '  
    while move not in [0,1,2,3,4,5,6,7,8] or not freespace(position,move):
        print ('What is your next move? (1-9)')
        move = input()
        return int(move-1)
