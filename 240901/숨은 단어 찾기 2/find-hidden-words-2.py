# arr n*m
# /print/ number of 'LEE' in horizontal, vertical, and diagonal directions
# 1) check start with 'L' 
# 2) move 8 direction and in_range == True
# 3) next char is 'E' and 'E'


n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]

dxs, dys = [0, 1, 1, 1, 0, -1, -1, -1],[1, 1, 0, -1, -1, -1, 0, 1]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < m
cnt = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] != 'L':
            continue
        for dx, dy in zip(dxs, dys):
            if not in_range(i+dx*2, j+dy*2):
                continue
            
            if arr[i+dx][j+dy] == 'E' and arr[i+dx*2][j+dy*2] == 'E':
                cnt += 1

print(cnt)