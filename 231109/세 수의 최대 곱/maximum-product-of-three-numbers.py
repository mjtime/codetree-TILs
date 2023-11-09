n = int(input())
arr = list(map(int, input().split()))

arr.sort()

test_arr = []
test_arr.append(arr[-1] * arr[-2] * arr[-3])
test_arr.append(arr[0] * arr[1] * arr[2])
test_arr.append(arr[0] * arr[1] * arr[-1])

print(max(test_arr))