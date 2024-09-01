# squence A consists of N elements
# squence B consists of M elements
# beautiful sequence B is a state where the same operation is applied to each element, or the sequence itself.
# => ex) B[4, 6, 7] -> [3, 5, 7] or [5, 3, 6] or [4, 6, 7], etc...
# //print// how many beautiful squence are in A ?

n = int(input())
arr_n = [int(input()) for _ in range(n)]
m = int(input())
arr_m = [int(input()) for _ in range(m)]
beautiful_idx = []
max_n = max(arr_n)
min_n = min(arr_n)

def permute(arr):
    result = []
    if len(arr) == 1:
        return [arr]
    
    for i in range(len(arr)):
        remaining_elements = arr[:i] + arr[i+1:]
        for p in permute(remaining_elements):
            result.append([arr[i]]+p)
    return result


for i in range(n - m + 1):
    arr_permutaion1 = permute(arr_m[::])
    for perm in arr_permutaion1:
        if arr_n[i:i+m] == perm:
            beautiful_idx.append(i+1)
    
    temp_arr2 = arr_m[::]
    while True:
        if max(temp_arr2) >= max_n:
            break
        temp_arr2 = [x+1 for x in temp_arr2]
        arr_permutaion2 = permute(temp_arr2)
        for perm in arr_permutaion2:
            if arr_n[i:i+m] == perm:
                beautiful_idx.append(i+1)
    
    temp_arr3 = arr_m[::]
    while True:
        if min(temp_arr3) <= min_n:
            break
        temp_arr3 = [x-1 for x in temp_arr3]
        arr_permutaion3 = permute(temp_arr3)
        for perm in arr_permutaion3:
            if arr_n[i:i+m] == perm:
                beautiful_idx.append(i+1)

print(len(beautiful_idx))
beautiful_idx.sort()
for idx in beautiful_idx:
    print(idx)