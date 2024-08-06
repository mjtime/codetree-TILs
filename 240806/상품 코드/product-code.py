class Product:
    def __init__(self, name, code):
        self.name = name
        self.code = code

item1 = Product("codetree", 50)

name, code = tuple(input().split())
item2 = Product(name, int(code))

print(f"product {item1.code} is {item1.name}")
print(f"product {item2.code} is {item2.name}")