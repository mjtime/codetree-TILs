def star(n):
    if n < 1:
        return
    
    star(n-1)
    print('*' * n)

n = int(input())
star(n)