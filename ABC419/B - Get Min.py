q = int(input())
query = [list(map(int, input().split())) for _ in range(q)]
bag = []

for i in range(q):
  if query[i][0] == 1:
    bag.append(query[i][1])
    bag.sort()
  elif query[i][0] == 2:
    print(bag.pop(0))