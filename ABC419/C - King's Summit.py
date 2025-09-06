n = int(input())
r = []
c = []

for _ in range(n):
  x, y = map(int, input().split())
  r.append(x)
  c.append(y)

x = max(r) - min(r)
y = max(c) - min(c)
print((max(x, y) + 1) // 2)