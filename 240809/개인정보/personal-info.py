class User:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

arr = [input().split() for _ in range(5)]

users = [User(name, int(h), float(w)) for name, h, w in arr]

users.sort(key = lambda x:x.name)

print("name")
for u in users:
    print(u.name, u.height, u.weight)

print()
print("height")
users.sort(key = lambda x:-x.height)
for u in users:
    print(u.name, u.height, u.weight)