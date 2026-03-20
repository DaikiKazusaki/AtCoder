n, s = map(int, input().split())
t = list(map(int, input().split()))

if t[0] > s:
    print("No")
    exit()

for i in range(n-1):
    if t[i+1] - t[i] > s:
        print("No")
        exit()

print("Yes")