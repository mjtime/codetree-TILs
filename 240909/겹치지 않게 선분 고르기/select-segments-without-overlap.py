n = int(input())
lines = [list(map(int, input().split())) for _ in range(n)]
select_lines = []
ans = 0

def overlap(curr_idx, base_line):
    curr_x1, curr_x2 = lines[curr_idx]
    base_x1, base_x2 = lines[base_line]
    if curr_x1 <= base_x1 <= curr_x2:
        return True
    elif curr_x1 <= base_x2 <= curr_x2:
        return True
    else:
        return False

def check_lines(curr_idx):
    for base_line_idx in select_lines:
        if overlap(curr_idx, base_line_idx):
            return True
    return False

def choose(curr_num):
    global ans
    if curr_num >= n:
        ans = max(ans, len(select_lines))
        # print(select_lines)
        # print("==================")
        return
    
    for curr_idx in range(n):
        if not check_lines(curr_idx):
            select_lines.append(curr_idx)
            choose(curr_num+1)
            select_lines.pop()
        else:
            choose(curr_num + 1)
    
    return
    
choose(0)
print(ans)