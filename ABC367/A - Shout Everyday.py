a, b, c = map(int, input().split())

if b < c:
    if b < a < c:
        print('No')
    else:
        print('Yes')
else:
    if c < a < b:
        print('Yes')
    else:
        print('No')