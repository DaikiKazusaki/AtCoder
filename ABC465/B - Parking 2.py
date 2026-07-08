x, y, l, r, a, b = map(int, input().split())

ans = 0

for i in range(a, b):
    if i < l:
        ans += y
    elif l <= i < r:
        ans += x
    else:
        ans += y

print(ans)