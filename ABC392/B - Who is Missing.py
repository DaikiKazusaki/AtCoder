n, m = map(int, input().split())
a = list(map(int, input().split()))
x = []

for i in range(1, n + 1):
    if not i in a:
        x.append(i)

print(len(x))
for i in range(len(x)):
    print(x[i], end = " ")