n = int(input())
p = [0] + list(map(int, input().split()))     # 見つめている人
q = [0] + list(map(int, input().split()))     # ゼッケンの番号
s = [0] * (n + 1)

for i in range(1, n + 1):
    s[q[i]] = q[p[i]]

print(*s[1:])