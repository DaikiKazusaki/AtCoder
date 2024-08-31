n = int(input())
h = list(map(int, input().split()))
t = 0
i = 0

for item in h:
    num = item // 5
    t += num * 3
    item -= num * 5

    while True:
        if item <= 0:
            break

        t += 1

        if t % 3 == 0:
            item -= 3
        else:
            item -= 1

print(t)