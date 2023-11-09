n = int(input())
arr = list(map(int, input().split()))

arr.sort()

test1 = arr[-1] * arr[-2] * arr[-3]
test2 = arr[0] * arr[1] * arr[-1]

print(max(test1, test2))