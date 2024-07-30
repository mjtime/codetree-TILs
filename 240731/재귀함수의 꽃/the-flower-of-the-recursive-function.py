def count(n):
    if n < 1:
        return

    print(n, end = ' ')
    count(n - 1)
    print(n, end = ' ')

n = int(input())
count(n)