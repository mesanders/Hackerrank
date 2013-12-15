#!/usr/bin/python

# Head ends here
# Head ends here
def next_move(posr, posc, board, direction='right'):
    #posr is the vertical column and posc is the horizontal column
    moveToGetToTop = "f"
    for i in range (4):
        if board[0][i] == 'd' and posc != 0:
            moveToGetToTop = "LEFT"
            break
        elif board[0][i] == 'd' and posc != 0:
            moveToGetToTop = "UP"
            break
        
    if board[posr][posc] == 'd':
        print("CLEAN")
    elif moveToGetToTop != 'f':
        print(moveToGetToTop)
    elif posc < 4 and posr % 2 == 0:
        print("RIGHT")
    elif posc > 0 and posr % 2 != 0:
        print("LEFT")
    else:
        print("DOWN")

# Tail starts here
# Tail starts here
if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    next_move(pos[0], pos[1], board, '')