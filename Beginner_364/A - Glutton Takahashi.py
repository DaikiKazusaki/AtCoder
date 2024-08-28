n = int(input())
s = []
for _ in range(n):
    s.append(input())
result = 'Yes'

for i in range(n - 2):
    if s[i] == 'sweet' and s[i + 1] == 'sweet':
        result = 'No'

print(result)