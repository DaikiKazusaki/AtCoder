n = int(input())
a = list(map(int, input().split()))

for i in range(n - 2):
    if a[i] == a[i + 1] == a[i + 2]:
        print('Yes')
        exit()

print('No')