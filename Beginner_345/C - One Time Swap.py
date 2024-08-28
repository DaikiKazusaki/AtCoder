s = list(input())
n = len(s)
count = 0

for i in range(n):
    for j in range(i + 1, n):
        if i == 0 and j == 1:
            count += 1
        elif s[i] != s[j]:
            count += 1


print(count)