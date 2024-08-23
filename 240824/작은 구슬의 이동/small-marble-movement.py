# 1초마다 한 칸, 상<->하,좌<->우
# 맨 처음이 1행 1열 => [n-1][n-1]형태로 저장해야함
# r행, c열
# 벽에 부딪히면 방향 변경 (1s 소요)
# t초 이후 구슬 위치

n, t = map(int, input().split())
dxs, dys = [0, 1, -1, 0],[1, 0, 0, -1] # 방향 = 3 - 방향
mapper = {'R': 0, 'D':1, 'U':2, 'L':3}

r, c, d = input().split()
r = int(r) - 1
c = int(c) - 1
dir_num = mapper[d]
def in_range(x, y):
    return 0<= x and x < n and 0<=y and y<n

for _ in range(t):
    nx = r + dxs[dir_num]
    ny = c + dys[dir_num]
    if not in_range(nx, ny):
        dir_num = 3 - dir_num
    else:
        r, c = nx, ny

# 첫 칸이 1열 1행이라고 문제에 제시되어 있기에 +1
print(r+1, c+1)