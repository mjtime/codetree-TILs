# n개 방에 최대 100명의 인원
# 1번 방 부터 n번방까지 반시계 방향으로 이동
# (출력) 1~n번방에서 각각 시작했을 때 제일 적은 거리의 합?

import sys

n = int(input())
house = [int(input()) for _ in range(n)]

min_dist = sys.maxsize
for i in range(n):
    hap_dist = 0
    for j in range(n):
        if i > j:
            dist = n - i + j
        else:
            dist = j - i
        hap_dist += (dist * house[j])
    min_dist = min(min_dist, hap_dist)

print(min_dist)