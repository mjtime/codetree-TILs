def check_369(m):
    if '3' in str(m):
        return True
    if '6' in str(m):
        return True
    if '9' in str(m):
        return True
    else:
        return False

def check_num(n):
    if n % 3 == 0 or check_369(n):
        return(True)
    else:
        False


a, b = map(int, input().split())
cnt = 0
for i in range(a, b+1):
    if check_num(i):
        cnt += 1
print(cnt)