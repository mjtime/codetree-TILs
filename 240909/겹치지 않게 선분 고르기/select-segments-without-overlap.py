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

def choose(curr_idx):
    global ans
    # 더 이상 선택할 수 없는 경우, 정답 업데이트
    ans = max(ans, len(select_lines))
    
    # 선분의 시작점을 기준으로 가지치기
    for next_idx in range(curr_idx, n):
        if not check_lines(next_idx):  # 겹치지 않는 경우에만 선택
            select_lines.append(next_idx)  # 선분 선택
            choose(next_idx + 1)  # 다음 선분 선택
            select_lines.pop()  # 선택 취소
    
    return

choose(0)
print(ans)

# print(check_lines(4))