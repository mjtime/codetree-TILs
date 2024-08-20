n, m, k = map(int, input().split())
students = [0 for _ in range(n)]
ans = -1
for _ in range(m):
    num = int(input())
    students[num - 1] += 1
    if k in students:
        ans = students.index(k) + 1
        break
print(ans)