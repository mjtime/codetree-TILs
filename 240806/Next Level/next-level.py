class User:
    def __init__(self, name = "", level=1):
        self.name = name
        self.level = level

user1 = User()
user1.name = "codetree"
user1.level = 10
print(f'user {user1.name} lv {user1.level}')

name, level = tuple(input().split())

user2 = User()
user1.name = name
user1.level = int(level)

print(f'user {user1.name} lv {user1.level}')