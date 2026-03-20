# ネタ
ABCを用いたプログラミングに関するオリジナルの問題を考案しています．

## [ABC405 - B - Not All](https://atcoder.jp/contests/abc405/tasks/abc405_b)
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

## [ABC407 - C - Security 2](https://atcoder.jp/contests/abc407/tasks/abc407_c)
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

## [ABC408 - C - Not All Coverd](https://atcoder.jp/contests/abc408/tasks/abc408_c)
砲台 $i$ が守っている城壁（ $l_i$ ～ $r_i$ ）を記録する方法としてimos法がある．  
imos法とは， $l_i$ ～ $r_i$ がカバーしている領域を1次元の配列を利用して解く方法である．記録する内容は以下の通り．
1. array[ $l_i-1$ ]はカバー開始なので，1を加算
1. array[ $r_i$ ]はカバー終了なので，1を減算
1. arrayを前から順番に足していくことで，array[$i$]のカバー数を計算
```python
n, m = map(int, input().split())

covered = [0] * (n + 1)

for _ in range(m):
    l, r = map(int, input().split())
    covered[l-1] += 1
    covered[r] -= 1

for i in range(1, n):
    covered[i] += covered[i-1]

ans = float("inf")

for i in range(n):
    ans = min(ans, covered[i])

print(ans)
```