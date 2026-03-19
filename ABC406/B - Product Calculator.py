n, k = map(int, input().split())
a = list(map(int, input().split()))

answer = 1

for i in range(n):
    answer *= a[i]

    if answer >= 10 ** k:
        answer = 1

print(answer)