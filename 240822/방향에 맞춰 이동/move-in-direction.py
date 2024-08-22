x, y = 0, 0
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
n = int(input())
for _ in range(n):
    dir_str, go = input().split()
    go = int(go)
    if dir_str == 'E':
        dir_num = 0
    elif dir_str == 'S':
        dir_num = 1
    elif dir_str == 'W':
        dir_num = 2
    else:
        dir_num = 3
    x, y = x + dx[dir_num]*go, y + dy[dir_num]*go
print(x, y)