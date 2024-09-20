def change_one_order(lst_result, idx):
    lst_result[idx], lst_result[idx + 1] = lst_result[idx + 1], lst_result[idx]

def change_orders(lst_line, lst_result):
    for line_idx, _ in lst_line:
        change_one_order(lst_result, line_idx - 1)

def choose(curr_num):
    global ans_num_of_line, seen_combinations

    if curr_num >= ans_num_of_line:  # 현재 저장된 최소 가로줄보다 더 많은 가로줄은 연산하지 않음
        return

    if result == ans_result:
        ans_num_of_line = min(ans_num_of_line, len(choose_lines))
        return

    for i in range(curr_num, m):
        if lines[i] in choose_lines:  # 이미 담긴 줄이면 패스
            continue

        choose_lines.append(lines[i])
        change_one_order(result, (lines[i][0]) - 1)

        combination_key = tuple(sorted(map(tuple, choose_lines)))  # 조합을 정렬하여 튜플로 변환
        if combination_key in seen_combinations:  # 중복된 조합 체크
            choose_lines.pop()  # 현재 줄 선택 취소
            change_one_order(result, (lines[i][0]) - 1)  # 원래 상태로 되돌림
            continue

        seen_combinations.add(combination_key)  # 조합 추가
        choose(curr_num + 1)

        change_one_order(result, (choose_lines[-1][0]) - 1)
        choose_lines.pop()

    return

n, m = map(int, input().split())
lines = [list(map(int, input().split())) for _ in range(m)]

ans_result = [x + 1 for x in range(n)]  # 목표 결과 값

choose_lines = []
result = [x + 1 for x in range(n)]  # 계산을 위한 초기 값
seen_combinations = set()  # 조합 중복 확인을 위한 set

# 줄 높이에 따라 줄 정렬
lines.sort(key=lambda x: (x[1], x[0]))

# 기존에 주어진 사다리 타기 진행한 결과
change_orders(lines, ans_result)

ans_num_of_line = m
choose(0)
print(ans_num_of_line)