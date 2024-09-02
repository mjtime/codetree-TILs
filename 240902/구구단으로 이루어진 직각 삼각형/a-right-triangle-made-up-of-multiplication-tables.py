n = int(input())
for i in range(1,n+1):
    for j in range(1,n+2-i):
        print(f"{i} * {j} = {i*j}",end=" ")
        if j!=n+1-i:
            print('/',end=" ")
        else:
            print()