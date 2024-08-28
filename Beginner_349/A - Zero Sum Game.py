n = int(input())
a = list(map(int, input().split()))
sum = 0
for _ in range(n - 1):
    sum += a[_]

print(sum * (-1))