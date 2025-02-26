s = list(input())
count = 0

for i in range(len(s)):
    for j in range(i, len(s)):
        for k in range(j, len(s)):
            if s[i] == "A" and s[j] == "B" and s[k] == "C" and j - i == k - j:
                count += 1

print(count)
