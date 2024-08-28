s = list(input())
t = list(input())
ans = list()
i = 0

for _ in range(len(t)):
    if s[i] == t[_]:
        i += 1
        ans.append(_ + 1)

for _ in ans:
    print(_, end = ' ')