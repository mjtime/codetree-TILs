# squence A consists of N elements
# squence B consists of M elements
# beautiful sequence B is a state where the same operation is applied to each element, or the sequence itself.
# => ex) B[4, 6, 7] -> [3, 5, 7] or [5, 3, 6] or [4, 6, 7], etc...
# //print// how many beautiful squence are in A ?

# algorithm
# 1) A의 부분수열과 B수열 오름차순 정렬
# 2) temp_arr를 B수열 만큼 만듦
# 3) temp_arr에 '1)'의 각 자리수를 뺀 값을 담음
# 4) temp의 모든 값이 같으면 아름다운 수열

n = int(input())
arr_n = [int(input()) for _ in range(n)]
m = int(input())
arr_m = [int(input()) for _ in range(m)]
beautiful_idx = []
sorted_m = sorted(arr_m)
for i in range(n-m+1):
    sorted_n = sorted(arr_n[i:i+m])
    for j in range(m):
        if j == 0:
            diff = sorted_n[j]-sorted_m[j]
        else:
            if diff != sorted_n[j]-sorted_m[j]:
                break
        if j == m-1:
            beautiful_idx.append(i+1)

print(len(beautiful_idx))
for idx in beautiful_idx:
    print(idx)