# n : 행(row), m : 열(column)

n, m = map(int, input().split())
arr = [[0]*m for _ in range(n)]
dir_num = 0
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
x, y = 0, 0
arr[x][y] = 1
def in_range(x, y):
    return 0 <= x and x < n and 0<= y and y<m

for i in range(2, n*m + 1):
    nx = x + dxs[dir_num]
    ny = y + dys[dir_num]

    if not in_range(nx, ny) or arr[nx][ny] != 0:
        dir_num = (dir_num + 1) % 4
        
    x = x + dxs[dir_num]
    y = y + dys[dir_num]

    arr[x][y] = i

for i in range(n):
    for j in range(m):
        print(arr[i][j], end = ' ')
    print()