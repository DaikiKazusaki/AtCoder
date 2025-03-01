n, q = map(int, input().split())
query = [list(map(int, input().split())) for _ in range(q)]
nest = [[i + 1] for i in range(n)]

for list in query:
    count = 0

    if list[0] == '1':
        p = list[1]
        h = list[2]
        

    elif list[0] == '2':
        for _ in range(n):
            if len(nest[_]) > 1:
                count += 1
            print(count)