n = int(input())
s = []

for i in range(n):
    input_str = input()
    s.append(input_str)

s.sort(key = len)

for i in range(n):
    print(s[i], end = "")