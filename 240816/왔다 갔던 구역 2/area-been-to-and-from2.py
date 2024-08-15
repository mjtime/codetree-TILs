n = int(input())
# offset => n = 100 번씩 x=10인 경우 100x10 = 1000
# lenth => +-값 보정, -1000 ~ 1000 => 0 ~ 2000
arr_len = 2001
arr = [0 for _ in range(arr_len)]
now = 1000

for _ in range(n):
    distance, dic = input().split()
    distance = int(distance)

    if dic =='R':
        distance = now + distance
    else:
        distance = now - distance
    
    start = min(now, distance)
    end = max(now, distance)
    
    # 지점일 경우 end + 1,
    # start, end가 점이라고 할때
    # 구간이기 때문에 점과 점사이에 +1해준다고 생각
    # start = 1, end = 3인 경우 => 1~2, 2~3 총 두곳에 +1
    arr[start:end] = [x+1 for x in arr[start:end]]
    
    # R일 경우 오른쪽 방향으로 설정(now -> end 바라봄)
    # L일 경우 왼쪽 방향으로 설정(start <- now 바라봄)
    if dic == 'R':
        now = end
    else:
        now = start
#2번 이상 지나간 구간 = 전체 - 1번 이하로 지나간 구간
print(arr_len-arr.count(0)-arr.count(1))