n = int(input())
# -100 ≤ x1 < x2 ≤ 100
offset = 100
arr = [0 for _ in range(200)]

for _ in range(n):
    a, b = map(int, input().split())
    a += offset - 1
    b += offset - 1
    arr[a:b] = [x + 1 for x in arr[a:b]]

print(max(arr))