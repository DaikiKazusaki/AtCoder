n = int(input())
a = list(map(int, input().split()))
s = []
t = []

for i in range(n - 1):
    s_i, t_i = map(int, input().split())
    s.append(s_i)
    t.append(t_i)

for i in range(n - 1):
    if a[i] >= s[i]:
        a[i + 1] += a[i] // s[i] * t[i]

print(a[n - 1])