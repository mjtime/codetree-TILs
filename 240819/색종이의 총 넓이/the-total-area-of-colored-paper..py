# 8x8, 64넓이 n장
# 좌측 하단 꼭짓점 좌표
# 겹치는 경우 한번만 넓이 포함

OFFSET = 100
rects = [[0]*200 for _ in range(200)]

def drow(x, y):
    for i in range(x, x+8):
        for j in range(y, y+8):
            rects[i][j] = 1

n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    x += OFFSET
    y += OFFSET
    drow(x, y)

area = 0
for i in range(200):
    area += rects[i].count(1)
print(area)