# Omok board game
# board size: 19*19, board number is start 1, end 19
# /print/ (1) winner (2) winner's middle location(x, y)
SIZE = 19
board = [list(map(int, input().split())) for _ in range(SIZE)]

def find_r(x, y, p):
    for k in range(1, 5):
        if board[x][y+k] != p:
            return False
    return True

def find_d(x, y, p):
    for k in range(1, 5):
        if board[x+k][y] != p:
            return False
    return True

def find_rd(x, y, p):
    for k in range(1, 5):
        if board[x+k][y+k] != p:
            return False
    return True

def find_ld(x, y, p):
    for k in range(1, 5):
        if board[x+k][y-k] != p:
            return False
    return True
x, y = 0, 0
winner = 0
finish = False
for i in range(SIZE):
    for j in range(SIZE):
        if board[i][j] != 0:
            if j <= SIZE - 5 and find_r(i, j, board[i][j]):
                winner = board[i][j]
                x, y = i+1, j+3
                finish = True
                break
            elif i <= SIZE - 5 and find_d(i, j, board[i][j]):
                winner = board[i][j]
                x, y =i+3, j+1
                finish = True
                break
            elif i <= SIZE - 5 and j <= SIZE - 5 and find_rd(i, j, board[i][j]):
                winner = board[i][j]
                x, y =i+3, j+3
                finish = True
                break
            elif i <= SIZE - 5 and j >= 4 and find_ld(i, j, board[i][j]):
                winner = board[i][j]
                x, y =i+3, j-1
                finish = True
                break
    if finish:
        break

print(winner)   
if finish:
    print(x, y)