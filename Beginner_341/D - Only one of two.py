import math

n, m, k = map(int, input().split())
lcm = math.lcm(n, m)
only_one_divided = []

for i in range(1, lcm):
    if (i % n == 0 and i % m != 0) or (i % n != 0 and i % m == 0):
        only_one_divided.append(i)
    
if len(only_one_divided) == 1:
    q = k // 2
    r = k % 2
    print(q * 2 + r)
else:
    q = k // lcm
    r = k % lcm
    print(q * lcm + r)
