n = int(input())
arr = list(map(int, input().split()))

def lcm(num, idx):
    if idx == -1:
        return num
    for i in range(max(arr[idx], num), arr[idx]*num + 1):
        if i % arr[idx] == 0 and i % num == 0:
            return lcm(i, idx-1)

print(lcm(arr[n-1], n-2))