# 절대값으로 변경, 값을 반환하지 않는 함수

n = int(input())
_list = list(map(int, input().split()))

def change_abs(arr):
    for i in arr:
        if i < 0:
            print(i*-1, end =' ')
        else:
            print(i, end =' ')

change_abs(_list[:])