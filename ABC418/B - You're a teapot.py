s = input()

n = len(s)
ans = 0.0
for i in range(n):
  if s[i] != 't':
    continue

  for j in range(i + 2, n):
    if s[j] != 't':
      continue

    x = sum(1 for ki in range(i, j + 1) if s[ki] == 't')
    length = j - i + 1

    item = (x - 2) / (length - 2)
    if item > ans:
      ans = item

print(f"{ans:.17f}")

