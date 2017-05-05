def check4win(position,counter):
    return ((position[0]==counter and position[1]==counter and position[2]==counter)or
            (position[3]==counter and position[4]==counter and position[5]==counter)or
            (position[6]==counter and position[7]==counter and position[8]==counter)or
            (position[0]==counter and position[3]==counter and position[6]==counter)or
            (position[1]==counter and position[4]==counter and position[7]==counter)or
            (position[2]==counter and position[5]==counter and position[8]==counter)or
            (position[0]==counter and position[4]==counter and position[8]==counter)or
            (position[2]==counter and position[4]==counter and position[6]==counter))
