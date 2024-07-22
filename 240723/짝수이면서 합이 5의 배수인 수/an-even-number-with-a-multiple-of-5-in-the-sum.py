def check_num(n):
    ten = n // 10
    one = n % 10
    hap = ten + one
    if n % 2 == 0 and hap % 5 == 0:
        return "Yes"
    else:
        return "No"

n = int(input())
print(check_num(n))