# ネタ
ABCを用いたプログラミングに関するオリジナルの問題を考案しています．

## ABC405

### [B - Not All](https://atcoder.jp/contests/abc405/tasks/abc405_b)
`for i in range(n + 1):`を`for i in range(n):`とするミス．  
変数 $i$ の範囲は $i = 0, 1, ..., n$ であるはずだが，`range(n)`では $i = 0, 1, ..., n-1$ しかとらないため不適．
```python
n, m = map(int, input().split())
a = list(map(int, input().split()))

for i in range(n + 1):
    if len(set(a)) == m:
        a.pop()
    else:
        print(i)
        exit()
```

## ABC407

### [C - Security 2](https://atcoder.jp/contests/abc407/tasks/abc407_c)
`print(num_a + num_b + s[-1])`を`print(num_a + num_b)`として配列 $s$ の最後の要素を足し忘れるミス．  
ループ内では隣り合う桁の差分を計算するため，配列の最後の要素は別で加算する必要がある．
```python
s = [int(c) for c in input()]

num_a = len(s)
num_b = 0

for i in range(len(s) - 1):
    if s[i] > s[i+1]:
        num_b += s[i] - s[i+1]
    elif s[i] < s[i+1]:
        num_b += 10 + s[i] - s[i+1]

print(num_a + num_b + s[-1])
```
