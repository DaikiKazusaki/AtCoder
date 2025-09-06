n, q = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
cxv = [input().split() for _ in range(q)]
ans = 0

for i in range(n):
  ans += min(a[i], b[i])

for i in range(q):
  c, x, v = cxv[i]
  x = int(x) - 1
  v = int(v)

  if c == 'A':
    ans -= min(a[x], b[x])
    a[x] = v
    ans += min(a[x], b[x])
  else:
    ans -= min(a[x], b[x])
    b[x] = v
    ans += min(a[x], b[x])

  print(ans)  