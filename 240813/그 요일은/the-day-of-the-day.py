# 2024년 기준, 윤년 존재하기 때문에 2월은 29일까지
m1, d1, m2, d2 = map(int, input().split())
target_week = input()
week = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
month_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
num_of_target_week = week.index(target_week)
def cal_days(m, d):
    for i in range(m-1):
        d += month_days[i]
    return d

days = (cal_days(m2, d2) - cal_days(m1, d1))

num_of_week = days // 7
num_of_day = days % 7

if num_of_day < num_of_target_week:
    print(num_of_week)
else:
    print(num_of_week + 1)