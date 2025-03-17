q = int(input())
query = [list(map(int, input().split())) for _ in range(q)]
card = [0] * 100

for i in range(q):
    if query[i][0] == 1:
        card.append(query[i][1])
    elif query[i][0] == 2:
        print(card[len(card) - 1])
        card.pop()