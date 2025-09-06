n = int(input())
a = list(map(int, input().split()))
counter = {}
ans = 0

for i, a in enumerate(a):
  ans += counter.get(i - a, 0)
  counter[i + a] = counter.get(i + a, 0) + 1

print(ans)