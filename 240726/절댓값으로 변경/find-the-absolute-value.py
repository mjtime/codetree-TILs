# 절대값으로 변경, 값을 반환하지 않는 함수

n = int(input())
arr = list(map(int, input().split()))

def change_abs(arr):
    for i in range(n):
        if arr[i] < 0:
            arr[i] = arr[i]*-1
    return

change_abs(arr)

for elem in arr:
    print(elem, end =' ')