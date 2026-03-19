a, b = map(int, input().split())

if a % b <= b // 2:
    print(a // b)
else:
    print(a // b + 1)