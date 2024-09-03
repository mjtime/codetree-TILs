# the snail shape is in the direction of ↓ → ↑ ← rotation
# fill in snail shape with numbers from 1 ro n*m

n, m = map(int, input().split())
arr = [[0]*m for _ in range(n)]

def in_range(x, y):
    return 0<=x<n and 0<=y<m
dxs, dys = [0,1,0,-1],[1,0,-1,0]
dir_num = 1
x, y = 0,0
arr[x][y] = 1

for i in range(n*m-1):
    nx = x+dxs[dir_num]
    ny = y+dys[dir_num]
    if not in_range(nx, ny) or arr[nx][ny] != 0:
        dir_num = (dir_num+3)%4
        nx = x+dxs[dir_num]
        ny = y+dys[dir_num]
    x, y = nx, ny
    arr[x][y] = i+2

for i in range(n):
    for j in range(m):
        print(arr[i][j], end = ' ')
    print()