class Bomb:
    def __init__(self, code, color, sec):
        self.code = code
        self.color = color
        self.sec = sec

code, color, sec = tuple(input().split())

bomb1 = Bomb(code, color, int(sec))

print(f"code : {bomb1.code}")
print(f"color : {bomb1.color}")
print(f"second : {bomb1.sec}")