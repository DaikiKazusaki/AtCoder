s = list(input())
check = True

for _ in range(len(s)):
    if _ == 0:
        if not s[_] == '<':
            check = False
            break
    elif _ == len(s) - 1:
        if not s[_] == '>':
            check = False
            break
    else:
        if not s[_] == '=':
            check = False
            break

if check:
    print('Yes')
else:
    print('No')