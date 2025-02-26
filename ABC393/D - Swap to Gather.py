n = int(input())
s = input()
c1 = s.count('1')
now = 0
ans = 0

for c in s:
    if c == '0':
        ans += min(now, c1 - now)
    else:
        now += 1

print(ans)