text = input()
pattern = input()

def is_match(start_idx):
    n = len(text)
    m = len(pattern)

    # text가 pattern 글자수보다 작으면 false
    if start_idx + m - 1 >= n:
        return False
    
    for j in range(m):
        if text[start_idx + j] != pattern[j]:
            return False
    
    return True

def find_index():
    for i in range(len(text)):
        if is_match(i):
            return i
    return -1


print(find_index())