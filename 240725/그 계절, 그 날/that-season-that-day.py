y, m , d = map(int, input().split())

#윤년 확인
def check_leap_year(y):
    if y % 4 == 0 and y % 100 != 0:
        return True
    elif y % 4 == 0 and y % 100 == 0 and y % 400 == 0:
        return True
    return False

# 존재하는지 확인
def check_day(y, m, d):
    end31 = [1,3,5,7,8,10,12]
    end30 = [4,6,9,11]
    if m == 2:
        if check_leap_year(y):
            if d < 30:
                return True
        else:
            if d < 29:
                return True
    elif m in end31:
        if d < 32:
            return True
    elif m in end30:
        if d < 31:
            return True
    return False

# 계절확인
def check_season(m):
    if 3 <= m <= 5:
        return "Spring"
    elif 6 <= m <= 8:
        return "Summer"
    elif 9 <= m <= 11:
        return "Fall"
    else:
        return "Winter"

if check_day(y, m, d):
    print(check_season(m))
else:
    print(-1)