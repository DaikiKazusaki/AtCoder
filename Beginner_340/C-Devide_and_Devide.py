# メモ化による再帰の高速化
## from functools import cache
## @cache

from functools import cache

@cache
def f(N):
    if N == 1:
        return 0
    else:
        return f(N // 2) + f((N + 1) // 2) + N

print(f(int(input())))