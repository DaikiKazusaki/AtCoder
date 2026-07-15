n, m = map(int, input().split())

size = [-1] * m

for i in range(n):
    c, s = map(int, input().split())

    if size[c - 1] < s:
        size[c - 1] = s

print(*size)