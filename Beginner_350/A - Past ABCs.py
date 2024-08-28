s = list(input())
num = 100 * int(s[3]) + 10 * int(s[4]) + int(s[5])

if num != 316 and 0 < num < 350:
    print('Yes')
else:
    print('No')