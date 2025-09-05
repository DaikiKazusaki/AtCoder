x, y = map(int, input().split())
ans = [0] * 10
ans[0] = x
ans[1] = y

for i in range(8):
  ans_tmp = str(ans[i] + ans[i+1])
  ans[i+2] = int(ans_tmp[::-1])


print(ans[-1])