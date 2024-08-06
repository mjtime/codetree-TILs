n, k, t = map(str, input().split())
n = int(n)
k = int(k)
arr = []

for _ in range(n):
    word = input()
    if word[:len(t)] == t:
        arr.append(word)

arr.sort()
print(arr[k-1])