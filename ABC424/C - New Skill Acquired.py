n = int(input())
ab = []
skills = [0] * n

for _ in range(n):
  a,b = map(int, input().split())
  if a > b:
    a, b = b, a
  ab.append([a, b, _])

ab.sort()

for i in range(n):
  a, b, idx = ab[i]

  if a == b == 0:
    skills[idx] = 1
  elif skills[a-1] == 1 or skills[b-1] == 1:
    skills[idx] = 1

print(skills.count(1))