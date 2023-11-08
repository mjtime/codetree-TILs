n = int(input())
arr = list(map(int, input().split()))
arr_tmp = arr.copy()
min_val = min(arr)

cnt = arr.count(min_val)

for i in range(cnt):
    arr_tmp.remove(min_val)

if len(arr_tmp)>0:
    min_val = min(arr_tmp)
    if 1==arr_tmp.count(min_val):
        print(arr.index(min_val) + 1)
    else:
        print(-1)
else:
    print(-1)