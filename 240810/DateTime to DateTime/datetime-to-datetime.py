d1, h1, m1 = 11, 11, 11
d2, h2, m2 = map(int, input().split())

def check_day():
    if d1>d2:
        return False
    elif h1>h2:
        return False
    elif m1 > m2:
        return False
    else:
        return True
# 1day = 24 hour = 1440min
if check_day():
    day = d2 - d1
    hour = h2 - h1
    mins = m2 - m1

    print(day*24*60 + hour*60 + mins)
else:
    print(-1)