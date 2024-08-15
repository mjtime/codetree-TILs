# 끝점이 닿는 경우 포함
n = int(input())
lines = [0 for _ in range(101)] # x1, x2 값 보정대신 101로 설정
for _ in range(n):
    x1, x2 = map(int, input().split())
    lines[x1:x2 + 1] = [x + 1 for x in lines[x1:x2+1]]

print(max(lines))