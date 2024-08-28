n, q = map(int, input().split())
t = list(map(int, input().split()))
num = [True] * n

for _ in range(q):
    num[t[_] - 1] = not num[t[_] - 1]

print(num.count(True))