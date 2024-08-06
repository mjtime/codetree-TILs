n = int(input())
arr = list(map(int, input().split()))

arr.sort()

def find_mid(i):
    idx_mid = i // 2
    print(arr[idx_mid], end=' ')

for i in range(n+1):
    if i % 2 != 0:
        find_mid(i)