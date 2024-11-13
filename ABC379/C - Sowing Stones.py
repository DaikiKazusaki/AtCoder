n, m = map(int, input().split())
x = list(map(int, input().split()))
a = list(map(int, input().split()))

difference = 0
remainder = 0
ans = 0

for i in range(m - 1):
    difference = x[i + 1] - x[i]

    if a[i] < difference + remainder:
        print(-1)
        exit()
    else:
        remainder = a[i] - difference
        ans += difference * (difference - 1) // 2

ans += (a[m - 1] + remainder) * (a[m - 1] + remainder - 1) // 2

print(ans)