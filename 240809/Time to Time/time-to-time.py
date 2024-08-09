s_hour, s_mins, e_hour, e_mins = map(int, input().split())

if e_mins < s_mins:
    e_mins += 60
    e_hour -= 1

mins = e_mins - s_mins
hour = e_hour - s_hour

print(hour * 60 + mins)