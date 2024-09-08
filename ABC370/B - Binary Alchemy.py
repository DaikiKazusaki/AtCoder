n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
i = 1

for j in range(1, n + 1):
    if i >= j:
        i = a[i - 1][j - 1]
    elif i < j:
        i = a[j - 1][i - 1]

print(i)