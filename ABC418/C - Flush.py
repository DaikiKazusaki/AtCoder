# pythonで二分探索を行うためのモジュール
import bisect

n, q = map(int, input().split())
a = list(map(int, input().split()))
b = [int(input()) for _ in range(q)]

a.sort()
# 累積和(0 ~ i番目のリストの和)を計算
prefix_sum = [0] * (n + 1)
for i in range(n):
  prefix_sum[i + 1] = prefix_sum[i] + a[i]

for num in b:
  if a[-1] < num:
    print(-1)
    continue

  index = bisect.bisect_left(a, num)
  ans = prefix_sum[index] + (num - 1) * (n - index)

  print(ans + 1)