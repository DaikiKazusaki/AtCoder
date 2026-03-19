n, k = map(int, input().split())
a = [1] * k
s = k

for i in range(k, n + 1):
    s += a[i - 1] - a[i - k - 1]
    a.append(s % 1000000000)

print(a[n])