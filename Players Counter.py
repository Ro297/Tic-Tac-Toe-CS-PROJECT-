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


PlayerCounter()
