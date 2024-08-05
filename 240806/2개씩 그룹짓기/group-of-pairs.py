n = int(input())
arr = list(map(int, input().split()))

arr.sort()
max_num = 0
hap = 0
for i in range(1, n+1):
    hap = arr[i-1] + arr[n*2-i]
    # print(hap, i-1, n-i,arr[i], arr[n-1-i])
    max_num = max(hap, max_num)

print(max_num)