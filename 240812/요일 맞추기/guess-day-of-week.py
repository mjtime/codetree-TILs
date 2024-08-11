# 윤년이 아닌 경우, 2월은 28일까지 존재
def check_week(n):
    if n == 1:
        return "Mon"
    elif n == 2:
        return "Tue"
    elif n == 3:
        return "Wed"
    elif n == 4:
        return "Thu"
    elif n == 5:
        return "Fri"
    elif n == 6:
        return "Sat"
    else:
        return "Sun"

month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
m1, d1, m2, d2 = map(int, input().split())
day1, day2 = d1, d2

for i in range(m1-1):
    day1 += month_days[i]
for i in range(m2-1):
    day2 += month_days[i]

day1_week_num = day1 % 7
day2_week_day = day2 % 7
week = []

for i in range(7):
    week.insert(day1_week_num % 7, i+1)
    day1_week_num += 1

print(check_week(week[day2_week_day]))