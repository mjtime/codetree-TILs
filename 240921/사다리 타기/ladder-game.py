def change_one_order(lst_result, idx):
    temp = lst_result[idx]
    lst_result[idx] = lst_result[idx+1]
    lst_result[idx+1] = temp

def change_orders(lst_line, lst_result):
    for line_idx, _ in lst_line:
        change_one_order(lst_result, line_idx-1)

def choose(curr_num):
    global ans_num_of_line
        
    if ans_result == result:
        ans_num_of_line = min(ans_num_of_line, len(choose_lines))
        return
    
    for i in range(curr_num, m):
        if lines[i] in choose_lines: # 이미 담긴 줄이면 패스
            continue

        choose_lines.append(lines[i])
        change_one_order(result, (lines[i][0]) - 1) # 줄에 의해 수 바꿈
        choose(curr_num + 1)
        change_one_order(result, (choose_lines[-1][0]) - 1) # 마지막 줄에 의해 바뀐 수 돌려 놓음
        choose_lines.pop()


    return

n, m = map(int, input().split())
lines = [list(map(int, input().split())) for _ in range(m)]
ans_result = [x+1 for x in range(n)]

choose_lines = []
result = [x+1 for x in range(n)]

# 줄 높이에 따라 줄 정렬
lines.sort(key = lambda x:(x[1], x[0]))

# 기존에 주어진 사다리 타기 진행한 결과
change_orders(lines, ans_result)

ans_num_of_line = m
choose(0)
print(ans_num_of_line)