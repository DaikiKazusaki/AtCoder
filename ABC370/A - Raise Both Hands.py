l, r = map(int, input().split())

if l == 1 and r == 0:
    print('Yes')
elif l == 0 and r == 1:
    print('No')
else:
    print('Invalid')