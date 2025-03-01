n = int(input())
ans = [['.' for _ in range(n)] for _ in range(n)]

for i in range(n):
    j = n - i
    if i <= j and i % 2 == 1:
        for _ in range(i, j):
            for index in range(i, j):
                ans[_][index] = '.'
    elif i <= j and i % 2 == 0:
        for _ in range(i, j):
            for index in range(i, j):
                ans[_][index] = '#'

for i in range(n):
    for j in range(n):
        print(ans[i][j], end='')
    print()