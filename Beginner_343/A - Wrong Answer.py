a, b = map(int, input().split())

for _ in range(1, 9):
    if _ != a + b:
        print(_)
        break