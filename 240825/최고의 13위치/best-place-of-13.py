n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

ans = 0
for i in range(n):
    for j in range(n-2):
        hap = 0
        hap = arr[i][j] + arr[i][j+1] + arr[i][j+2]
        ans = max(ans, hap)

print(ans)