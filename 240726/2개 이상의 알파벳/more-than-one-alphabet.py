a = input()

def check(a):
    for i in range(0, len(a)-1):
        if a[i] != a[i+1]:
            return True
    return False

if check(a):
    print("Yes")
else:
    print("No")