n, t = map(int, input().split())
score = [0 for _ in range(n)]
ab = [list(map(int, input().split())) for _ in range(t)]

for _ in range(t):
    a = ab[_][0]
    b = ab[_][1]
    score[a - 1] += b
    print(len(set(score)))