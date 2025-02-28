n, m = map(int, input().split())
s = [list(input()) for _ in range(n)]
t = [list(input()) for _ in range(m)]

for a in range(n - m + 1):
    for b in range(n - m + 1):
        is_ok = True
        for i in range(m):
            for j in range(m):
                if s[a + i][b + j] != t[i][j]:
                    is_ok = False

        if is_ok:
            print(a  + 1, b + 1)