n = int(input())
arr = list(map(int, input().split()))

def find_mid(i):
    sorted_arr = sorted(arr[:i])
    print(sorted_arr[i//2], end=' ')

for i in range(n+1):
    if i % 2 != 0:
        find_mid(i)