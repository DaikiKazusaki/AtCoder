n = int(input())
a = list(map(int, input().split()))
dp_even = 0
dp_odd = -float('inf')

for _ in a:
    tmp = dp_even
    dp_even = max(dp_odd + 2 * _, dp_even)
    dp_odd = max(tmp + _, dp_odd)

print(max(dp_even, dp_odd))