# 0 or 1로 격자판 채움, 1에 폭탄 위치할 예정
# 폭탄은 1~3 타입이 올 수 있음
# 어떤 폭탄을 배치해야 가장 큰 범위 초토화 가능한가?
# (초토화 범위: 폭탄 위치 포함, 중복 위치는 1개로 나타냄)
# /*/ 폭탄의 개수에 따라 다중 for문 개수 증가됨 => 백트래킹
import copy

n = int(input())
bomb_grid = [list(map(int, input().split())) for _ in range(n)]
bomb_grid_temp = copy.deepcopy(bomb_grid)
bomb_type_x = [[-1,-2,1,2], [0,1,0,-1], [1,1,-1,-1]]
bomb_type_y = [[0,0,0,0], [1,0,-1,0], [1,-1,-1,1]]
bomb_locations = []
ans = -1

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def cal_bomb_range(x, y):
    bomb_num = bomb_grid[x][y] - 1
    for dx, dy in zip(bomb_type_x[bomb_num], bomb_type_y[bomb_num]):
        nx = x+dx
        ny = y+dy
        if in_range(nx, ny):
            bomb_grid_temp[nx][ny] = 1

def count_bomb_range():
    zero_hap = 0
    for i in range(n):
        zero_hap += bomb_grid_temp[i].count(0)

    return n*n - zero_hap

def find_bomb():
    for i in range(n):
        for j in range(n):
            if bomb_grid[i][j] > 0:
                bomb_locations.append([i, j])
                if len(bomb_locations) >= 10:
                    return

def choose(curr_bomb):
    global ans, bomb_grid_temp
    
    while True:
        if curr_bomb > len(bomb_locations):
            for i in range(len(bomb_locations)):
                cal_bomb_range(bomb_locations[i][0], bomb_locations[i][1])

            ans = max(ans, count_bomb_range())
            bomb_grid_temp = copy.deepcopy(bomb_grid)
            return
        
        for i in range(1, 4):
            x = bomb_locations[curr_bomb-1][0]
            y = bomb_locations[curr_bomb-1][1]
            bomb_grid[x][y] = i
            choose(curr_bomb +1)
            
        return
        
find_bomb()
choose(1)
print(ans)