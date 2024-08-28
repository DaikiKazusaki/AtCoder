n, x ,y, z = map(int, input().split())

if (x <= z and z <= y) or (y <= z and z <= x):
    print('Yes')
else:
    print('No')