start_time = 11
d2, h2, m2 = map(int, input().split())

def check_day():
    if start_time<d2:
        return True
    elif start_time==d2 and start_time<h2:
        return True
    elif start_time==d2 and start_time==h2 and start_time<=m2 :
        return True
    else:
        return False
# 1day = 24 hour = 1440min
if check_day():
    day = d2 - start_time
    hour = h2 - start_time
    mins = m2 - start_time

    print(day*24*60 + hour*60 + mins)
else:
    print(-1)