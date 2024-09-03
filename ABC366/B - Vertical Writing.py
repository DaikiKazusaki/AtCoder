n = int(input())
s = []
for i in range(n):
    s.append(list(input()))

m = max(len(s[i]) for i in range(n))

t = [['*'] * n for _ in range(m)]

for i in range(n):
    for j in range(len(s[i])):
        t[j][n - i - 1] = s[i][j]
for i in range(m):
    while t[i][-1] == "*":
        t[i].pop()
    print("".join(t[i]))