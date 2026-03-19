q = int(input())
query = [input().split() for _ in range(q)]

ticket = []

for i in range(q):
    if query[i][0] == "1":
        ticket.append(query[i][1])
    elif query[i][0] == "2":
        print(ticket[0])
        ticket.pop(0)