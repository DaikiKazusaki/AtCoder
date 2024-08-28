def Mancala2(a, b, n):
    if b == []:
        return a
    index = b.pop(0)
    ball = a[index]
    a[index] = 0
    q = ball // n
    r = ball % n
    for i in range(n):
        a[i] += q
    for i in range(r):
        a[(index + i + 1) % n] += 1
    return Mancala2(a, b, n)

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ans = Mancala2(a, b, n)
for i in range(n):
    print(ans[i], end = ' ')