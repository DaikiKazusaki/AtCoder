s = [int(c) for c in input()]

num_a = len(s)
num_b = 0

for i in range(len(s) - 1):
    if s[i] > s[i+1]:
        num_b += s[i] - s[i+1]
    elif s[i] < s[i+1]:
        num_b += 10 + s[i] - s[i+1]

print(num_a + num_b + s[-1])