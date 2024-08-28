n = int(input())
a = list(map(int, input().split()))

b = sorted(a)
print(a.index(b[n - 2]) + 1)