class User:
    def __init__(self, name = "codetree", level=10):
        self.name = name
        self.level = level

user1 = User()
print(f'user {user1.name} lv {user1.level}')
name, level = tuple(map(str, input().split()))
user1.name = name
user1.level = level

print(f'user {user1.name} lv {user1.level}')