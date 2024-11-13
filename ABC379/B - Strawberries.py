n, k = map(int, input().split())
s = list(input())
list = []
count = 0
ans = 0

for item in s:
    if item == 'O':
        count += 1
    elif item == 'X' and count > 0:
        list.append(count)
        count = 0
    
list.append(count)

for i in range(len(list)):
    ans += list[i] // k

print(ans)