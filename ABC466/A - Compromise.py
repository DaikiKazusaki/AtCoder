n = int(input())
x = list(map(int, input().split()))

result = True

for i in range(n):
    if x[i] >= 0:
        result = False
        break

print("Yes" if result else "No")