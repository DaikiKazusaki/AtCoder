n = int(input())
a = list(map(int, input().split()))

if len(set(a)) == n:
    print(-1)
    exit()

ans_list = []

for i in range(n):
    for j in range(i + 1, n):
        if a[i] == a[j]:
            ans_list.append(j - i + 1)
            break

print(min(ans_list))