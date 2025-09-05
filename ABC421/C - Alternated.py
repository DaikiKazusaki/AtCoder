n = int(input())
s = list(input())

a_idx = [i for i in range(2*n) if s[i] == 'A']

ans_1 = 0
for i in range(n):
  ans_1 += abs(2*i - a_idx[i])

ans_2 = 0
for i in range(n):
  ans_2 += abs((2*i + 1) - a_idx[i])

print(min(ans_1, ans_2))