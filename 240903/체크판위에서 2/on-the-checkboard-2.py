# (0, 0)에서 (r, c)로 이동
r,c = map(int, input().split())
arr = [list(input().split()) for _ in range(r)]

cnt = 0
# 시작점(0, 0) 범위 제외
for i in range(1, r):
    for j in range(1, c):
        # 마지막(r, c)는 도착지점이라 범위 제외
        for k in range(i+1, r-1):
            for l in range(j+1, c-1):
                if arr[0][0] != arr[i][j] and \
                   arr[i][j] != arr[k][l] and \
                   arr[k][l] != arr[r-1][c-1]:
                    cnt += 1
print(cnt)