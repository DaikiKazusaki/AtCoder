n, a, b = map(int, input().split())
d = list(map(int, input().split()))
ans = False

d = [_ % (a + b) for _ in d]
d = set(d)
d = sorted(d)

for i in range(len(d) - 1):
    if (d[i + 1] - d[i]) % (a + b) > b:
        ans = True
        break
if (d[len(d) - 1] - d[0]) % (a + b) > b:
    ans = True

if ans:
    print('Yes')
else:
    print('No')