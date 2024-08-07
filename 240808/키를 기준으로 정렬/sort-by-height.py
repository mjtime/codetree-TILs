class User:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

n = int(input())
arr = [tuple(input().split()) for _ in range(n)]
users = [User(name, height, weight) for name, height, weight in arr]

users.sort(key = lambda x : x.height)

for user in users:
    print(user.name, user.height, user.weight)