class Number:
    def __init__(self, num, idx = -1):
        self.num = num
        self.idx = idx

n = int(input())
arr = list(map(int, input().split()))
sequence = [Number(num) for num in arr]

sorted_sequence = sorted(sequence, key = lambda x:x.num)

for i, number in enumerate(sorted_sequence):
    number.idx = i+1

for number in sequence:
    print(number.idx, end =' ')