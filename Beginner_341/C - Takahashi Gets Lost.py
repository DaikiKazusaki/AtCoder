h, w, n = map(int, input().split())
t = list(input())
print(t)
s = [[]for _ in range(h)]
for _ in range(h):
    s[_] = list(input())

ans = []

for _ in range(h):
    for __ in range(w):
        count = 0
        for i in t:
            x = _
            y = __

            if s[x][y] == "#":
                ans.append(False)
                break

            if t[i] == "U":
                x = x - 1
            elif t[i] == "D":
                x = x + 1
            elif t[i] == "L":
                y = y - 1
            elif t[i] == "R":
                y = y + 1

print(h * w - ans.count(False))