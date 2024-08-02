def sequence(n):
    if n == 1:
        return 2
    elif n == 2:
        return 4
    else:
        return sequence(n-1)*sequence(n-2)%100

n = int(input())
print(sequence(n))