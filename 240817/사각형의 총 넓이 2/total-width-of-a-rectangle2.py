OFFSET = 100
rectangles = [[0]*200 for _ in range(200)]

def drow(x1,y1,x2,y2):
    for i in range(x1, x2):
        for j in range(y1, y2):
            rectangles[i][j] = 1
            
n = int(input())
for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    drow(x1+OFFSET, y1+OFFSET, x2+OFFSET, y2+OFFSET)

cnt = 0
for i in range(200):
    cnt += rectangles[i].count(1)
print(cnt)