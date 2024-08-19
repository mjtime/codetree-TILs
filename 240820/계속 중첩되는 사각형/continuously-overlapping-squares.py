OFFSET = 100
rects = [[0]*200 for _ in range(200)]
n = int(input())

def drow(x1, y1, x2, y2, num):
    for i in range(x1, x2):
        for j in range(y1, y2):
            rects[i][j] = num

for i in range(n):
    x1, y1, x2, y2 = map(lambda x:int(x)+OFFSET, input().split())
    drow(x1, y1, x2, y2,(i+2)%2)

area = 0
for i in range(200):
    area += rects[i].count(1)
print(area)