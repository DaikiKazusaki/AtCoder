import math

n = int(input())
x = int(math.pow(n, 1/3))

for i in range(x + 1, 0, -1):
    num = i ** 3
    if num > n:
        continue
    if str(num) == str(num)[::-1]:
        break

print(num)