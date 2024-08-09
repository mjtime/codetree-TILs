class User:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

n = int(input())

users = []
for _ in range(n):
    n, h, w = tuple(input().split())
    users.append(User(n, int(h), int(w)))

users.sort(key = lambda x:(x.height, -x.weight))

for u in users:
    print(u.name, u.height, u.weight)