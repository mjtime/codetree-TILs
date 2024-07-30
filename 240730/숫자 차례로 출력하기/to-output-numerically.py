def one_n(n):
    if n<1:
        return

    one_n(n-1)
    print(n, end = ' ')

def n_one(n):
    if n<1:
        return
    
    print(n, end = ' ')
    n_one(n-1)
    

n = int(input())
one_n(n)
print()
n_one(n)