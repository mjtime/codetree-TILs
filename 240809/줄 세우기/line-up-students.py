class Student:
    def __init__(self, height, weight, num = 0):
        self.height = height
        self.weight = weight
        self.num = num

n = int(input())
students = []
for i in range(n):
    height, weight = map(int, input().split())
    students.append(Student(height, weight, i+1))

students.sort(key = lambda x:(-x.height, -x.weight, x.num))

for s in students:
    print(s.height, s.weight, s.num)