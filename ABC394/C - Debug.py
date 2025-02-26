s = list(input())

for i in range(len(s) - 1, 0, -1):
    if s[i - 1] == "W" and s[i] == "A":
        s[i - 1] = "A"
        s[i] = "C"

print("".join(s))