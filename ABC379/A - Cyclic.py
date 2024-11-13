n = int(input())

a = n // 100
b = (n - a * 100) // 10
c = n - a * 100 - b * 10

ans1 = 100 * b + 10 * c + a
ans2 = 100 * c + 10 * a + b

print(str(ans1) + ' ' + str(ans2))