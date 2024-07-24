a, o, c = map(str, input().split())
a = int(a)
c = int(c)

def plus(a, b):
    return a + b
def minus(a, b):
    return a - b
def times(a, b):
    return a * b
def divide(a, b):
    return a // b

if o == '+':
    print(a, o, c, "=", plus(a, c))
elif o == '-':
    print(a, o, c, "=", minus(a, c))
elif o == '*':
    print(a, o, c, "=", times(a, c))
elif o == '/':
    print(a, o, c, "=", divide(a, c))
else:
    print("False")