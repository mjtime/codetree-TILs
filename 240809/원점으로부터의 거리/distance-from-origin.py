class Point:
    def __init__(self, x, y, num, distance):
        self.x = x
        self.y = y
        self.num = num
        self.distance = distance
def cal_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

n = int(input())
points = []
x, y = 0, 0
for i in range(n):
    dx, dy = map(int, input().split())
    distance = cal_distance(x, y, dx, dy)
    points.append(Point(dx, dy, i+1, distance))

points.sort(key = lambda x:x.distance)

for p in points:
    print(p.num)