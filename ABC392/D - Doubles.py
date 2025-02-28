import collections  # Counterクラスのimport

n = int(input())
k, a = [], []
count_a = []

for i in range(n):
    input_ka = list(map(int, input().split()))
    k.append(input_ka[0])
    a.append(input_ka[1:])

for _ in k:
    for i in range(_):
        count = collections.Counter(i)
        count_a.append(count)

print(count_a)