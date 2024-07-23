y = int(input())

def is_leap_year(y):
    if y % 4 != 0:
        return "false"
    if y % 100 == 0 and y % 400 != 0:
        return "false"
    return "true"

print(is_leap_year(y))