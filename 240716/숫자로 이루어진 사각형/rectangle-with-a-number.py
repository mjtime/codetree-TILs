def print_n(n):
    num = 1
    for i in range(n):
        for j in range(n):
            print(num, end=' ')
            num += 1
            if num > 9:
                num = 1
        print()


n = int(input())
print_n(n)