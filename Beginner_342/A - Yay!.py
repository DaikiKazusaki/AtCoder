s = list(input())
cnt1 = cnt2 = 0
char1 = s[0]

for i in s:
    if i == char1:
        index1 = s.index(i) + 1
        cnt1 += 1
    else:
        char2 = s[1]
        index2 = s.index(i) + 1
        cnt2 += 1

if cnt1 == 1:
    print(index1)
else:
    print(index2)