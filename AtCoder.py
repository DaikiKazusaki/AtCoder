# atcoder頻出
# N は入力値
N = 1000

# 文字列を受け取る場合
A, B = input().split()

# 整数を受け取る場合
X, Y, Z = map(int, input().split())

# 小数を受け取る場合
H, M, S = map(float, input().split())

# 文字列を受け取る場合
A = input().split()

# 文字列を一文字ずつリストに格納する場合
A = list(input())

# 整数列を受け取る場合
A = list(map(int, input().split()))

# 小数列を受け取る場合
A = list(map(float, input().split()))

## 以下は空白で区切られた複数行の入力を受け取る場合

# 複数行の文字列を受け取る場合
A = [input().split() for _ in range(N)]

# 複数行の整数列を受け取る場合
A = [list(map(int, input().split())) for _ in range(N)]

# 複数行の小数列を受け取る場合
A = [list(map(float, input().split())) for _ in range(N)]

## 以下は空白で区切られていない複数行の入力を受け取る場合

# 複数行の文字列を受け取る場合
A = []
for i in range(N):
    A.append(list(input()))