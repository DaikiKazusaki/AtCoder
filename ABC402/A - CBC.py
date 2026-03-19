s = input()
answer = ""

for i in range(len(s)):
    if s[i] >= "A" and s[i] <= "Z":
        answer += s[i]

print(answer)