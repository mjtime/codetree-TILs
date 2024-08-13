binary = list(input())
num = 0
for i in range(len(binary)-1,-1,-1):
    if binary[i] == '1':
        num = num + 2**(len(binary)-1-i)

print(num)