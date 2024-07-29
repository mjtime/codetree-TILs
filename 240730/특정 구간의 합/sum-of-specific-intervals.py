n, m = map(int, input().split())
list_a = list(map(int, input().split()))
list_m = []
for _ in range(m):
    list_m.append(list(map(int, input().split())))
    

def cal_hap(idx):
    hap = 0
    start_idx = list_m[idx][0] - 1
    end_idx = list_m[idx][1]
    for num in list_a[start_idx:end_idx]:
        hap += num
    return hap

for idx in range(m):
    print(cal_hap(idx))