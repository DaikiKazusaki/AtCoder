x, y = map(int, input().split())

result = x + y if x + y <= 12 else x + y - 12

print(result)