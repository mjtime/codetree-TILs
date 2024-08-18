OFFSET = 1000
rects = [[0]*2000 for _ in range(2000)]
def drow1(x1, y1, x2, y2, num):
    for i in range(x1, x2):
        for j in range(y1, y2):
            rects[i][j] = num
max_x = -1
min_x = 3000

def input_rect(n):
    global max_x, min_x
    x1, y1, x2, y2 = map(int, input().split())
    drow1(x1+OFFSET, y1+OFFSET, x2+OFFSET, y2+OFFSET, n)
    max_x = max(x2+OFFSET, max_x)
    min_x = min(x1+OFFSET, min_x)

for _ in range(2):
    input_rect(1)
input_rect(0)

area = 0
for i in range(min_x, max_x):
    area += rects[i].count(1)

print(area)