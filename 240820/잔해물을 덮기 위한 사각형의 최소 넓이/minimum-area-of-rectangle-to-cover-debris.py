OFFSET = 1000
rects = [[0]*2000 for _ in range(2000)]

def drow(x1, y1, x2, y2, n):
    for i in range(x1, x2):
        for j in range(y1, y2):
            rects[i][j] = n


x1, y1, x2, y2 = map(lambda x:int(x) + OFFSET, input().split())
drow(x1,y1, x2, y2, 1)
points = [[x1, y1], [x1, y2-1], [x2-1, y2-1], [x2-1, y1]]
point_check = [1,1,1,1]
# 두번째 직사각형
a1, b1, a2, b2 = map(lambda x:int(x) + OFFSET, input().split())
drow(a1, b1, a2, b2, 0)

for i, (x, y) in enumerate(points):
    point_check[i] = rects[x][y]

min_x, max_x = x1, x2
min_y, max_y = y1, y2 

if point_check.count(0) == 2:
    # y 증가
    if point_check[0] == 0 and point_check[3] == 0:
        for dy in range(y1, y2):
            if rects[x1][dy] == 1:
                min_y = dy
                break

    # y 감소
    elif point_check[1] == 0 and point_check[2] == 0:
        for dy in range(y2-1, y1-1, -1):
            if rects[x1][dy] == 1:
                max_y = dy+1
                break
    # x 증가
    elif point_check[0] == 0 and point_check[1] == 0:
        for dx in range(x1, x2):
            if rects[dx].count(1) > 0:
                min_x = dx
                break
    # x 감소
    elif point_check[2] == 0 and point_check[3] == 0:
        for dx in range(x2-1, x1-1, -1):
            if rects[dx].count(1) > 0:
                max_x = dx + 1
                break
elif point_check.count(0) > 3:
    print(0)
    exit(0)

area = (max_x-min_x)*(max_y-min_y)

print(area)