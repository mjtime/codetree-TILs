# the state of comfort is when it is 3 colored up, down, left, right from the current point.
# //print// 1 if the current position is comfortable, 1, otherwise 0
# ======

n, m = map(int, input().split())
grid = [[0]*n for _ in range(n)]

dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
def in_range(x, y):
    return 0<= x and x<n and 0<= y and y< n

for i in range(m):
    cnt = 0
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    grid[x][y] = 1
    for dx, dy in zip(dxs, dys):
        nx = x + dx
        ny = y + dy
        if in_range(nx, ny) and grid[nx][ny] == 1:
            cnt += 1
    if cnt == 3:
        print(1)
    else:
        print(0)