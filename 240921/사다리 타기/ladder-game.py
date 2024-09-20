def change_one_order(lst_result, idx):
    lst_result[idx], lst_result[idx + 1] = lst_result[idx + 1], lst_result[idx]

def simulate_ladder(n, ladders):
    result = list(range(1, n + 1))
    for ladder, _ in ladders:
        change_one_order(result, ladder - 1)
    return result


def choose(curr_num, cnt):
    global ans_num_of_line

    if cnt >= ans_num_of_line:  # 현재 저장된 최소 가로줄 보다 더 많은 가로줄은 연산하지 않음
            return

    if simulate_ladder(n, choose_lines) == ans_result:
        ans_num_of_line = min(ans_num_of_line, cnt)
        return
    
    for i in range(curr_num, m):
        if lines[i] in choose_lines: # 이미 담긴 줄이면 패스
            continue

        choose_lines.append(lines[i])
        # change_one_order(result, (lines[i][0]) - 1)

        choose(curr_num + 1, cnt + 1)

        # change_one_order(result, (choose_lines[-1][0]) - 1)
        choose_lines.pop()

    return

n, m = map(int, input().split())
lines = [list(map(int, input().split())) for _ in range(m)]

# ans_result = list(range(1, n + 1)) # 목표 결과 값
ans_result = simulate_ladder(n, list(range(1, n + 1)))

choose_lines = []

# 줄 높이에 따라 줄 정렬
lines.sort(key = lambda x:(x[1], x[0]))

ans_num_of_line = m

choose(0, 0)

print(ans_num_of_line)