class User:
    def __init__(self, name, num, local):
        self.name = name
        self.num = num
        self.local = local

users = []
n = int(input())

for _ in range(n):
    name, num, local = tuple(input().split())
    users.append(User(name, num, local))

dic_last_idx = 0
for i in range(1, n):
    if users[dic_last_idx].name < users[i].name:
        dic_last_idx = i

print("name", users[dic_last_idx].name)
print("addr", users[dic_last_idx].num)
print("city", users[dic_last_idx].local)