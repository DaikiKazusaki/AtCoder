n, m = map(int, input().split())
a = list(map(int, input().split()))

a = [_ % m for _ in a]

print(a)