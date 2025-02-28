n, q = map(int, input().split())
query = [list(map(int, input().split())) for _ in range(q)]
nest = [[i + 1] for i in range(n)]

print(nest)

for i in range(q):
    if query[i][0] == 1:
        continue
    elif query[i][0] == 2:
        continue