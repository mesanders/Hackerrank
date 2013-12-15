#!/usr/bin/python

# Head ends here
# posr is vertical and posc is horizontal
def next_move(posr, posc, board):
    dirtyLocations = find_all_dirty(board)
    nearestDirty = find_closest_dirty(posr, posc, dirtyLocations)
    if board[posr][posc] == 'd':
        print("CLEAN")
    elif nearestDirty[1] > posc:
        print("RIGHT")
    elif nearestDirty[1] < posc:
        print("LEFT")
    elif (nearestDirty[0] > posr):
        print("DOWN")
    elif nearestDirty[0] < posr:
        print("UP")
    

def find_all_dirty(board):
    dirtyLocations = []
    for x in range(len(board)):
        for y in range(len(board[x])):
            if board[x][y] == 'd':
                dirtyLocations.append([x, y])
    return dirtyLocations
    
def find_closest_dirty(posr, posc, dirtyLocations):
    tempDistance = 999999 #this is a false value to show they are far away
    returnpoint = (posr, posc)
    for dirtylocation in dirtyLocations:
        tempY = abs(posr - dirtylocation[0])
        tempX = abs(posc - dirtylocation[1])
        if (tempX + tempY) < tempDistance:
            tempDistance = tempX + tempY
            returnpoint = (dirtylocation[0], dirtylocation[1])
    return returnpoint

# Tail starts here
# Tail starts here
if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    next_move(pos[0], pos[1], board)