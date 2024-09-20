def change_order(lst, idx):
    lst[idx], lst[idx + 1] = lst[idx + 1], lst[idx]

def simulate_order(lines, n):
    num = list(range(n))
    for idx in lines:
        change_order(num, idx)
    return num

def is_possible(lines, selected_lines, n):
    original_result = simulate_order([line[1] for line in lines], n)
    modified_result = simulate_order([line[1] for line in selected_lines], n)
    return original_result == modified_result

def find_min_lines(cnt, lines, selected_lines, n, m):
    if cnt == m:
        return len(selected_lines) if is_possible(lines, selected_lines, n) else float('inf')
    
    # 현재 줄을 포함한 경우
    selected_lines.append(lines[cnt])
    include_count = find_min_lines(cnt + 1, lines, selected_lines, n, m)
    
    # 현재 줄을 포함하지 않은 경우
    selected_lines.pop()
    exclude_count = find_min_lines(cnt + 1, lines, selected_lines, n, m)

    return min(include_count, exclude_count)

n, m = map(int, input().split())
lines = [tuple(map(int, input().split())) for _ in range(m)]
lines = [(b - 1, a - 1) for a, b in lines]  # 인덱스를 0부터 시작하도록 변환

# 줄을 위치에 따라 정렬
lines.sort()

ans = find_min_lines(0, lines, [], n, m)
print(ans)