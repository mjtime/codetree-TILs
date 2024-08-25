x1, x2, x3, x4 = map(int, input().split())

check = False
if x1<=x3 and x3<=x2:
    check = True
elif x1<=x4 and x4<=x2:
    check = True
elif x3<=x1 and x1<=x4:
    check = True
elif x3<=x2 and x2<=x4:
    check = True

if check:
    print("intersecting")
else:
    print("nonintersecting")