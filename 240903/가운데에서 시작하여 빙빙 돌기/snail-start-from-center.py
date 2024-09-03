# 2번 방향전환 마다 직진 수 +1 증가
n = int(input())
arr = [[0]*n for _ in range(n)]
x, y = n//2, n//2
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
dir_num = 0

def in_range(x, y):
    return 0<=x<n and 0<=y<n

arr[x][y] = 1
move  = 1
change_dir_cnt = 0
num = 2
end = True
while end:
    for _ in range(move):
        nx = x+dxs[dir_num]
        ny = y+dys[dir_num]
        if in_range(nx, ny):
            x, y = nx, ny
            arr[x][y] = num
            num += 1
        if num > n*n:
            end = False
            break
    #move만큼 직진 후 1회 -90도 회전
    dir_num = (dir_num+3)%4
    change_dir_cnt += 1

    #2번 방향 전환 후 이동수 1 증가
    if change_dir_cnt == 2:
        move+=1
        change_dir_cnt = 0

for i in range(n):
    for j in range(n):
        print(arr[i][j], end = ' ')
    print()