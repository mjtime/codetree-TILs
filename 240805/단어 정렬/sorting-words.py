n = int(input())
arr = [
    input()
    for _ in range(n)
]

arr.sort()

for elem in arr:
    print(elem)