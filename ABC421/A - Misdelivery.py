n = int(input())
s = [input() for _ in range(n)]
x , y = input().split()

num = int(x) - 1

if s[num] == y:
  print('Yes')
else:
  print('No')