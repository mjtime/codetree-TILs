n = int(input())
arr = list(map(int, input().split()))

def find_max(x, y):
    if x == 0 or y == -1:
        return arr[x]
    if arr[x] > arr[y]:
        return find_max(x, y-1)
    else:
        return find_max(y, y-1)
    
print(find_max(n-1, n-2))