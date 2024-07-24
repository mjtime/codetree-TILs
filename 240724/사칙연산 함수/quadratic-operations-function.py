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
    else:
        return "False"
    return str(result)

if o == '/' and c==0:
    print()
else:
    print(str(a), o, str(c), '=', cal(a, o, c))