n = int(input())
a = list(map(int, input().split()))
count = 0
tmp = 0

for i in range(n):
    a[i] -= 1

for i in range(n):
    print(a)
    print(a[i], i)
    if a[i] != i:
        count += 1
        tmp = a[i]
        a[i] = a[a[i]]
        a[a[i]] = tmp

print(count)