# ネタ
ABCを用いたプログラミングに関するオリジナルの問題を考案しています．

## ABC405

### B - Not All
`for i in range(n + 1):`を`for i in range(n):`とするミス．
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