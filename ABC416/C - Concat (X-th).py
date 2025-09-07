# 深さ優先探索を行う関数
def dfs(current, count):
  if count == k:
    ans.append(current)
    return
  
  for i in range(n):
    dfs(current + s[i], count + 1)

n, k, x = map(int, input().split())
s = [input() for _ in range(n)]
ans = []

dfs('', 0)
ans.sort()
print(ans[x - 1])