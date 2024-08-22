# L = -90, R = 90, F = + 1
dir_str = list(input())
x, y = 0, 0
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
now_dic = 3
for dir_c in dir_str:
    if dir_c == 'F':
        x = x + dx[now_dic]
        y = y + dy[now_dic]
    elif dir_c == 'R':
        now_dic = (now_dic+1)%4
    else:
        now_dic = (now_dic+3)%4

print(x, y)