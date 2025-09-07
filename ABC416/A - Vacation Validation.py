n, l, r = map(int, input().split())
s = list(input())

slice = s[l-1:r]

if all(x == 'o' for x in slice):
  print('Yes')
else:
  print('No')