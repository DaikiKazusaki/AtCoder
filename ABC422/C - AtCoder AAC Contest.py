t = int(input())
testcase = [list(map(int, input().split())) for _ in range(t)]

for i in range(t):
  print(min(testcase[i][0], testcase[i][2], sum(testcase[i])//3))