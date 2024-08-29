import sys

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
max_num_coin = -sys.maxsize

for i in range(n - 1):
    num_coin = 0
    for j in range(n - 2):
        num_coin += arr[i][j] + arr[i][j+1] + arr[i][j+2]

    for k in range(n - 2):
        num_coin += arr[i+1][k] + arr[i+1][k+1] + arr[i+1][k+2]
    max_num_coin = max(max_num_coin, num_coin)

print(max_num_coin)