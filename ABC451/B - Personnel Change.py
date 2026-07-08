n, m = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(n)]

before = [0] * m
after = [0] * m

for i in range(n):
    before[ab[i][0] - 1] += 1
    after[ab[i][1] - 1] += 1

for i in range(m):
    print(after[i] - before[i])