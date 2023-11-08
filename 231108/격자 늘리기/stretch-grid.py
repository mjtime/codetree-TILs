n, m, k = map(int, input().split())
arr = [
    input() for _ in range(n)
]

repeat = k//2
for line in arr:
    char = line[0]
    start = 0
    line_tmp = ''
    for i in range(m):
        if line[i] != char:
            char = line[i]
            end = i
            line_tmp += line[start:end]*k
            start = i
        if i == m-1:
            end = m
            line_tmp += line[start:end]*k
            for j in range(k):
                print(line_tmp)