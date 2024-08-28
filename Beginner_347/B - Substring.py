s = list(input())
ans = set()

for i in range(len(s)):
    for j in range(i + 1, len(s) + 1):
        ans.add(''.join(s[i:j]))

print(len(ans))