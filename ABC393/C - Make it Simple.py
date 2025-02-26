n, m = map(int, input().split())

list = [set() for _ in range(n)]
count = 0

for _ in range(m):
    u, v = map(int, input().split())

    if u == v:
        count += 1
    else:
        if v in list[u - 1]:
            count += 1
        else:
            list[u - 1].add(v)
            list[v - 1].add(u)

print(count)
