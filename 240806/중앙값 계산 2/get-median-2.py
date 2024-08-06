n = int(input())
arr = list(map(int, input().split()))

def find_mid(i):
    idx_mid = i // 2
    sorted_arr = sorted(arr[:i])
    print(sorted_arr[idx_mid], end=' ')

for i in range(n+1):
    if i % 2 != 0:
        find_mid(i)