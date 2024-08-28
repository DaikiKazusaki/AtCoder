n = int(input())
a = list(map(int, input().split()))

for _ in range(n - 1):
    print(a[_] * a[_ + 1], end = ' ')