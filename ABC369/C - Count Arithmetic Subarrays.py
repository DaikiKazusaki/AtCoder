n = int(input())
a = list(map(int, input().split()))
num_sub_a = []
count = 1
result = n

sub_a = [a[i + 1] - a[i] for i in range(n - 1)]

for i in range(1, len(sub_a)):
    if sub_a[i] == sub_a[i - 1]:
        count += 1
    else:
        num_sub_a.append(count)
        count = 1

if n != 1:
    num_sub_a.append(count)

for i in num_sub_a:
    result += i * (i + 1) // 2

print(result)