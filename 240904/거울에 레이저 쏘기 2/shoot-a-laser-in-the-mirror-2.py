n = int(input())
grid = [list(input()) for _ in range(n)]
k = int(input())
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
def setting_start(n, k):
    if k <= n:
        return -1, k-1, 1
    elif k <=n*2:
        return abs(n+1-k), n, 2
    elif k<= n*3:
        return n, n*3 - k,3
    else:
        return n*4 - k, -1, 0

def change_dir(mirror,dir_num):
    if mirror == '/':
        if dir_num == 0 or dir_num == 2:
            return (dir_num+3)%4
        else:
            return (dir_num+1)%4
    else:#'\\' == \
        if dir_num == 0 or dir_num == 2:
            return (dir_num+1)%4
        else:
            return (dir_num+3)%4

def in_range(x, y):
    return 0<=x<n and 0<=y<n

x, y, dir_num = setting_start(n, k)
cnt = 0
while True:
    nx = x+dxs[dir_num]
    ny = y+dys[dir_num]
    if not in_range(nx,ny):
        break
    x, y = nx, ny
    dir_num = change_dir(grid[x][y], dir_num)
    cnt += 1
print(cnt)