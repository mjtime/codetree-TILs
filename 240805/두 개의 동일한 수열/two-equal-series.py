n = int(input())
arr_a = list(map(int, input().split()))
arr_b = list(map(int, input().split()))

arr_a.sort()
arr_b.sort()

if arr_a == arr_b:
    print("Yes")
else:
    print("No")