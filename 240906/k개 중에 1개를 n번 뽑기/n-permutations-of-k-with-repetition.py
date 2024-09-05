# n 자리수 1~k의 숫자로 채움

k, n = map(int, input().split())
arr = []

def print_num():
    for c in arr:
        print(c, end = ' ')
    print()

def choose(curr_num):
    if curr_num == n+1:
        print_num()
        return
    
    for i in range(1, k+1):
        arr.append(i)
        choose(curr_num+1)
        arr.pop()
    
    return

choose(1)