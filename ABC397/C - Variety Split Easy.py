n = int(input())
a = list(map(int, input().split()))
max = 0
left = []
right = []

for i in range(n):
    left = a[:i]
    right = a[i:]
    max = len(set(left)) + len(set(right)) if len(set(left)) + len(set(right)) > max else max

print(max)