n, k = map(int, input().split())
a = set()

for _ in range(n):
    a.add(tuple(map(int, input().split())))

print(a)