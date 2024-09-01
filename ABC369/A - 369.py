a, b = map(int, input().split())
result = 0

if (a - b) == 0:
    result = 1
elif (a - b) % 2 != 0:
    result = 2
else:
    result = 3

print(result)