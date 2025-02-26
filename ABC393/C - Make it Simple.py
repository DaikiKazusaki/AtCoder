n, m = map(int, input().split())

graph = [set() for _ in range(n)]
count = 0

for _ in range(m):
    u, v = map(int, input().split())

    if u == v:
        count += 1
    else:
        if v in graph[u - 1]:
            count += 1
        else:
            graph[u - 1].add(v)
            graph[v - 1].add(u)

print(count)
