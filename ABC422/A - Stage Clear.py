s, e = map(int, input().split('-'))

if e == 8:
  print(str(s+1) + '-1')
elif s == 8 and e == 8:
  print('8-8')
else:
  print(str(s) + '-' + str(e+1))