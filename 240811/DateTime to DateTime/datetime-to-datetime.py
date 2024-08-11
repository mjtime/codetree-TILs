start_time = 11
d2, h2, m2 = map(int, input().split())

mins = (d2 * 24 * 60 + h2 * 60 + m2) - (start_time * 24 * 60 + start_time * 60 + start_time)

if mins < 0:
    print(-1)
else:
    print(mins)