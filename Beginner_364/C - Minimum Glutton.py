n, x, y = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
sum_a = sum_b = 0
a.sort(reverse = True)
b.sort(reverse = True)

for i in range(n):
    sum_a += a[i]
    sum_b += b[i]

    if sum_a > x or sum_b > y:
        break

print(i + 1)