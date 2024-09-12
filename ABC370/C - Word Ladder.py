s = list(input())
t = list(input())
n = len(s)
x = list()

while s != t:
    nxt = 'z' * n
    for i in range(n):
        if s[i] != t[i]:
            tmp = s[:i] + t[i] + s[i + 1:]
            nxt = min(nxt, tmp)
    x.append(nxt)
    s = nxt
    
print(len(x))
for _ in x:
    print(_)