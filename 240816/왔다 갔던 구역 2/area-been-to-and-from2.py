n = int(input())
arr_len = 2001
arr = [0 for _ in range(arr_len)]
now = 1000
# maxs = 0
# mins = 2000
for _ in range(n):
    distance, dic = input().split()
    distance = int(distance)
    # if dic == 'R':
    #     start = now
    #     end = distance + 1000 + 1
    # else:
    #     start = 1000 - distance
    #     end = now + 1
    if dic =='R':
        distance = now + distance
    else:
        distance = now - distance
    start = min(now, distance)
    end = max(now, distance)
    
    arr[start:end] = [x+1 for x in arr[start:end]]
    
    if dic == 'R':
        now = end
    else:
        now = start
    # print(dic, start, end, now)
    # print(arr[989:1003])
    # mins = min(mins, start)
    # maxs = max(maxs, end)
# print(mins, maxs)
# print(arr[mins:maxs])
# cnt = 0
# check = 0
# for num in arr[mins:maxs+1]:
#     if num > 1 and check != num:
#         cnt += 1
#     check = num
# print(cnt)
print(arr_len-arr.count(0)-arr.count(1))