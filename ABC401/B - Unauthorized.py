n = int(input())
s = [input() for _ in range(n)]

is_login = False
count = 0

for i in range(n):
    if s[i] == "login":
        is_login = True
    elif s[i] == "logout":
        is_login = False
    elif s[i] == "private" and not is_login:
        count += 1

print(count)