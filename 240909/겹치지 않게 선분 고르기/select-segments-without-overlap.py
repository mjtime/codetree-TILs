n = int(input())
lines = [list(map(int, input().split())) for _ in range(n)]
select_lines = []
ans = 0

def overlap(curr_idx, base_line):
    curr_x1, curr_x2 = lines[curr_idx]
    base_x1, base_x2 = lines[base_line]
    # print(curr_x1, curr_x2, base_x1, base_x2)
    # 선분이 겹치는 조건: 하나의 선분의 시작점이 다른 선분의 끝점보다 작거나 같고,
    # 끝점이 다른 선분의 시작점보다 크거나 같으면 겹친다.
    return not(curr_x2 < base_x1 or curr_x1 > base_x2)

def check_lines(curr_idx):
    for base_line_idx in select_lines:
        if overlap(curr_idx, base_line_idx):
            return True
    return False

def choose(curr_num):
    global ans
    if curr_num >= n:
        ans = max(ans, len(select_lines))
        # if len(select_lines)>2:
        #     print(select_lines)
        #     print("==================")
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

# print(check_lines(4))