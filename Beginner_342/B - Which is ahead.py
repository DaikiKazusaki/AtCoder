n = int(input())
p = list(input().split())
q = int(input())
ab = [input().split() for _ in range(q)]

for i in range(q):
    index1 = p.index(ab[i][0])
    index2 = p.index(ab[i][1])
    index = min(index1, index2)
    print(p[index])