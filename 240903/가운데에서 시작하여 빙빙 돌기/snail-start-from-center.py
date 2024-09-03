n = int(input())
arr = [[0]*n for _ in range(n)]
x, y = n//2, n//2
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
dir_num = 0

def in_range(x, y):
    return 0<=x<n and 0<=y<n

arr[x][y] = 1
k = 1
cnt = 0
num = 2
end = True
while end:
    # print('k', k)
    for _ in range(k):
        nx = x+dxs[dir_num]
        ny = y+dys[dir_num]
        x, y = nx, ny
        # print(num, x, y)
        arr[x][y] = num
        num += 1
        if num > n*n:
            end = False
            break
    dir_num = (dir_num+3)%4
    cnt += 1
    if cnt == 2:
        k+=1
        cnt = 0
# for i in range(1, n*n - 1):
#     nx = x+dxs[dir_num]
#     ny = y+dys[dir_num]
#     x, y = nx, ny
#     arr[x][y] = i+1
#     cnt += 1

    # if not in_range(nx, ny) or arr[nx][ny] != 0:
    #     dir_num = (dir_num+3)%4
    #     nx = x+dxs[dir_num]
    #     ny = y+dys[dir_num]
    # x, y = nx, ny
    # arr[x][y] = i+2

for i in range(n):
    for j in range(n):
        print(arr[i][j], end = ' ')
    print()