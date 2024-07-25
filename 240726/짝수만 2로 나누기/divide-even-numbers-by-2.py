n = int(input())
_list = list(map(int, input().split()))

# 값을 반환하지 않는 함수 사용
def half(arr):
    for i in arr:
        if i % 2 == 0:
            print(i//2, end=' ')
        else:
            print(i, end=' ')

half(_list[:])