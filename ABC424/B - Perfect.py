n, m, k = map(int, input().split())
list = [0] * n
ans = []

for i in range(k):
  a, b = map(int, input().split())
  list[a-1] += 1

  if list[a-1] == m:
    ans.append(a)

for _ in ans:
  print(_, end=' ')