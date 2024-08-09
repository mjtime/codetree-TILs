# 윤년이 아닌 해라고 가정, 2월은 28일까지 존재
m1, d1, m2, d2 = map(int, input().split())
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

day1 = 0
day2 = 0
for i in range(m1-1):
    day1 += days[i]
day1 += d1

for i in range(m2-1):
    day2 += days[i]
day2 += d2

print(day2 - day1 + 1)