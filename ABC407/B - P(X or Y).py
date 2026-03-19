x, y = map(int, input().split())
count = 0

for i in range(1, 7):
    for j in range(1, 7):
        if i + j >= x or abs(i - j) >= y:
            count += 1

print(count / 36 if count > 0 else 0)