m, d = map(int, input().split())

def check_day(m, d):
    end_one = [1, 3, 5, 7, 8, 10, 12]
    end_zero = [2, 4, 6, 9, 11]

    if m in end_one:
        if d<32:
            return "Yes"
    elif m in end_zero:
        if d<31:
            return "Yes"
    return "No"

print(check_day(m, d))