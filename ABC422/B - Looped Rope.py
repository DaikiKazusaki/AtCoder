h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]
count = 0
result = 'Yes'

for i in range(0, h):
  for j in range(0, w):
    if s[i][j] == '#':
      if i-1 >= 0 and s[i-1][j] == '#':
        count += 1
      if i+1 < h and s[i+1][j] == '#':
        count += 1
      if j-1 >= 0 and s[i][j-1] == '#':
        count += 1
      if j+1 < w and s[i][j+1] == '#':
        count += 1

      if count == 2 or count == 4:
        count = 0
      else:
        count = 0
        result = 'No'

print(result)