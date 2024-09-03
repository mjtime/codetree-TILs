# ignore out of grid code

n, t = map(int, input().split())

arr_move = list(input())
grid = [list(map(int, input().split())) for _ in range(n)]

dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
dir_num =3
x, y = n//2, n//2

def in_range(x, y):
    return 0<=x<n and 0<=y<n

hap = grid[x][y]

for move in arr_move:
    if move == 'L':
        dir_num = (dir_num+3)%4
    elif move =='R':
        dir_num = (dir_num+1)%4
    else:
        nx = x+dxs[dir_num]
        ny = y+dys[dir_num]
        if in_range(nx, ny):
            x, y = nx, ny
            hap += grid[x][y]

print(hap)