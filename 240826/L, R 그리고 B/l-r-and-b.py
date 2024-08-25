arr = [list(input()) for _ in range(10)]
lx, ly = 0,0
rx, ry = 0,0
bx, by = 0,0

def find_lrb(lx,ly,rx,ry,bx,by):
    find_cnt = 0
    for x in range(10):
        for y in range(10):
            if arr[x][y] == 'L':
                lx, ly = x, y
                find_cnt += 1
            elif arr[x][y] == 'R':
                rx, ry = x, y
                find_cnt += 1
            elif arr[x][y] == 'B':
                bx, by = x, y
                find_cnt += 1
        if find_cnt > 2:
            return lx,ly,rx,ry,bx,by

lx,ly,rx,ry,bx,by = find_lrb(lx,ly,rx,ry,bx,by)

cnt = abs(lx - bx) + abs(ly-by) -1
if lx == rx and rx == bx and min(ly, by) < ry and ry< max(ly, by):
    print(cnt+2)
elif ly==ry and ry==by and min(lx, bx) < rx and rx< max(lx, bx):
    print(cnt+2)
else:
    print(cnt)