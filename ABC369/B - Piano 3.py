n = int(input())
l = []
r = []
ans = 0

for i in range(n):
    a, s = input().split()
    if s == 'L':
        l.append(int(a))
    else:
        r.append(int(a))

for i in range(len(l) - 1):
    ans += abs(l[i + 1] - l[i])

for i in range(len(r) - 1):
    ans += abs(r[i + 1] - r[i])

print(ans)