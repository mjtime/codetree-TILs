def star(n):
    if n < 1:
        return
    
    print('* ' * n)
    star(n - 1)
    print('* ' * n)

n = int(input())
star(n)