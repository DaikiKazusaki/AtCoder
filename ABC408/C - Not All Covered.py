n, m = map(int, input().split())

covered = [0] * (n + 1)

for _ in range(m):
    l, r = map(int, input().split())
    covered[l-1] += 1
    covered[r] -= 1

for i in range(1, n):
    covered[i] += covered[i-1]

ans = float("inf")

for i in range(n):
    ans = min(ans, covered[i])

print(ans)