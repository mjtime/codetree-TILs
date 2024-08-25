# 하나의 집에서 각 가구원들의 이동 거리차가 적은 것 출력
import sys

n = int(input())
house = list(map(int, input().split()))

min_diff = sys.maxsize
for i in range(n):
    hap_diff = 0
    for j in range(n):
        diff = abs(i-j)*house[j]
        hap_diff += diff
    min_diff = min(min_diff, hap_diff)

print(min_diff)