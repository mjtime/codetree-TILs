import sys

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
max_num_coin = -sys.maxsize

check = False
for i in range(n):
    num_coin1, num_coin2, num_coin3 = 0, 0, 0
    for j in range(n - 2):
        num_coin1 = (arr[i][j] + arr[i][j+1] + arr[i][j+2])
        if n-2-j>3 and not check:
            for m in range(j+3, n-2):
                num_coin3 = (arr[i][m] + arr[i][m+1] + arr[i][m+2])
                max_num_coin = max(max_num_coin, num_coin1 + num_coin2)
                if m == n-2:
                    check = True
        else:
            for k in range(i+1, n):
                for l in range(n - 2):
                    num_coin2 = (arr[k][l] + arr[k][l+1] + arr[k][l+2])
                    # print(num_coin1, num_coin2)
                    max_num_coin = max(max_num_coin, num_coin1 + num_coin2)
                if i == n:
                    check = False
        



print(max_num_coin)