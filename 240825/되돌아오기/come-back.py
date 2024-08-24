MAX_LEN = 1000
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
x, y = 0, 0
mapper = {'E':0, 'S':1, 'W': 2, 'N': 3}


n = int(input())
cnt = 0
check = False
for i in range(n):
    c_dir, go = input().split()
    go = int(go)
    num_dir = mapper[c_dir]
    for j in range(go):
        x = x+dxs[num_dir]
        y = y+dys[num_dir]
        cnt += 1

        if x == 0 and y == 0:
            check = True
            break
    if check == True:
        break

if check == True:
    print(cnt)
else:
    print(-1)