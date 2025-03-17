x = list(input())
ans = 0
target = 'i'

for c in x:
    if c == target:
        target = 'o' if target == 'i' else 'i'
    else:
        ans += 1

if target == 'o':
    ans += 1

print(ans)