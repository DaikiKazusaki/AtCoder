n = int(input())
a = list(map(int, input().split()))

sum = sum(a)
answer = 0

for i in range(n):
    answer += a[i] * (sum - a[i])
    sum -= a[i]

print(answer)