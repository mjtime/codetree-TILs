# n 개의 체크포인트 존재
# 1 ~ n-1중 한 곳 제외하고 체크포인트 방문
# <출력> 어느 체크포인트를 제외해야 최단거리?
import sys

n = int(input())
points = [list(map(int, input().split())) for _ in range(n)]

min_dist = sys.maxsize

for i in range(1, n):
    hap_dist = 0
    x, y = points[0][0], points[0][1]
    for j in range(1,n):
        if j != i:
            hap_dist += (abs(x - points[j][0]) + abs(y - points[j][1]))
            x, y = points[j][0], points[j][1]
    min_dist = min(min_dist, hap_dist)

print(min_dist)