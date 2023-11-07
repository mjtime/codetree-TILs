n, k = map(int, input().split())
user_arr = []
max_idx = 0
max_score = 0
for i in range(n):
    loc, alpha = input().split()
    loc = int(loc)
    user_arr.append([loc, alpha])
    max_idx = max(max_idx, loc)
arr = [0] * max_idx

for idx, alpha in user_arr:
    score = 0
    if alpha == 'G':
        score = 1
    else:
        score = 2
    arr[idx-1] = score

for i in range(max_idx - k):
    hap = arr[i]
    for j in range(i+1, i+k+1):
        hap += arr[j]
    max_score = max(max_score, hap)

print(max_score)