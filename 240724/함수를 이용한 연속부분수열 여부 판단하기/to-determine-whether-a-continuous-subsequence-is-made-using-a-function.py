n1, n2 = map(int, input().split())

list_a = ''.join(map(str, input().split()))
list_b = ''.join(map(str, input().split()))

def match(a, b):
    if list_b in list_a:
        return "Yes"
    else:
        return "No"

print(match(list_a, list_b))