s = list(input())
t = list(input())
n = len(s)
x = []

while s != t:
    nxt = ['z'] * n  # nxtをリストとして初期化
    for i in range(n):
        if s[i] != t[i]:
            tmp = s[:i] + [t[i]] + s[i + 1:]  # t[i]をリストにして結合
            nxt = min(nxt, tmp)
    x.append(''.join(nxt))  # リストを文字列に変換して追加
    s = nxt

print(len(x))
for _ in x:
    print(_)
