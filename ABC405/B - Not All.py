n, m = map(int, input().split())
a = list(map(int, input().split()))

for i in range(n + 1):
    if len(set(a)) == m:
        a.pop()
    else:
        print(i)
        exit()