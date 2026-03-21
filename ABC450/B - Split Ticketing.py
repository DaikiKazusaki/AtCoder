n = int(input())
c = [[0]*(i+1) + list(map(int, input().split())) for i in range(n-1)]

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if c[i][j] + c[j][k] < c[i][k]:
                print("Yes")
                exit()

print("No")