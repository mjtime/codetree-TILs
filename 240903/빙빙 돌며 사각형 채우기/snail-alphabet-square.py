# algorithm
# 1) if the next space is not a blank or wall, rotate 90 degrees
# 2) ascii A:65 ~ Z:90
n, m = map(int, input().split())
arr = [[''] * m for _ in range(n)]
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
dir_num = 0
alphabet = 66
def in_range(x, y):
    return 0 <= x < n and 0<= y < m
x, y = 0, 0
arr[x][y] = chr(65)
for _ in range(n*m-1):
    dx = x+dxs[dir_num]
    dy = y+dys[dir_num]
    if not in_range(dx, dy) or arr[dx][dy] != '':
        dir_num = (dir_num+1)%4
        dx = x+dxs[dir_num]
        dy = y+dys[dir_num]
    x, y = dx, dy
    arr[x][y] = chr(alphabet)
    alphabet += 1
    if alphabet > 90:
        alphabet = 65

for i in range(n):
    for j in range(m):
        print(arr[i][j], end = ' ')
    print()