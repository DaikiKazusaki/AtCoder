r, x = map(int, input().split())

if r >= 1600 and r <= 2999 and x == 1:
    print("Yes")
elif r >= 1200 and r <= 2399 and x == 2:
    print("Yes")
else:
    print("No")