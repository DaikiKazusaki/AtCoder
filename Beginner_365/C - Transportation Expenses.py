n, m = map(int, input().split())
a = list(map(int, input().split()))

# sum(a) <= m ならば全員に支給可能
if sum(a) <= m:
    print('infinite')
# 条件を満たす数値の最大値を求める問題では二分探索を考える
else:
    ok, ng = 0, 1000000000
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        tmp = sum(min(mid, _) for _ in a)
        if tmp <= m:
            ok = mid
        else:
            ng = mid
    print(ok)