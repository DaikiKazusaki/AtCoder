n, m = map(int, input().split())
s = [(list(input())) for _ in range(n)]
ans = [0] * n
count_0 = 0
count_1 = 0

for i in range(m):
  for j in range(n):
    if s[j][i] == '0':
      count_0 += 1
    else:
      count_1 += 1
  
  if count_0 < count_1:
    for j in range(n):
      if s[j][i] == '0':
        ans[j] += 1
  else:
    for j in range(n):
      if s[j][i] == '1':
        ans[j] += 1

  count_0 = 0
  count_1 = 0

max = max(ans)

for i in range(n):
  if ans[i] == max:
    print(i + 1, end = ' ')