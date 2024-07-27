all_str = input()
want_str = input()

def check_str(a, w):
    if want_str in all_str:
        return True
    else:
        return False

def find_str(a, w):
    idx = 0

    for i in range(len(a)):
        if a[i] == w[idx]:
            idx += 1

            if idx == len(w):
                return i - idx +1
        else:
            idx = 0
        
            


    

if check_str(all_str, want_str):
    print(find_str(all_str, want_str))
else:
    print('-1')