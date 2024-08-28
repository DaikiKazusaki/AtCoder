n, k = map(int, input().split())
a = list(map(int, input().split()))
ans = list()

for _ in range(n):
    if a[_] % k == 0:
        ans.append(a[_] // k)

for _ in range(len(ans)):
    print(ans[_], end = ' ')