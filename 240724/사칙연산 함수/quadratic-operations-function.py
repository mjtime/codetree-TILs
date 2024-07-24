a, o, c = map(str, input().split())
a = int(a)
c = int(c)
def cal(x, y, z):
    result = 0
    if y == '+':
        result = x+z
    elif y == '-':
        result = x-z
    elif y == '/':
        result = x//z
    elif y == '*':
        result = x * z
    return str(result)

if o == '/' and c==0:
    print()
elif o not in ['+', '-', '*', '/']:
    print("False")
else:
    print(str(a), o, str(c), '=', cal(a, o, c))