n, k = map(int, input().split())
blocks = [0 for _ in range(n)]

for _ in range(k):
    a, b = map(int, input().split())
    # 값 보정
    a -= 1
    b -= 1
    blocks[a:b+1] = [x + 1 for x in blocks[a:b+1]]

print(max(blocks))