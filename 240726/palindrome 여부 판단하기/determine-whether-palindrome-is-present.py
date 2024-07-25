_str = input()

def is_palindrome(_str):
    reverse_str = ''
    for i in range(len(_str)-1, -1, -1):
        reverse_str += _str[i]
    return reverse_str

if is_palindrome(_str) == _str:
    print("Yes")
else:
    print("No")