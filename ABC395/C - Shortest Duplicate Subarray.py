n = int(input())
a = list(map(int, input().split()))

if len(set(a)) == n:
    print(-1)
    exit()

index_list = [[] for i in range(len(set(a)))]
new_list = list(set(a))

for i in range(n):
    num = a[i]
    index = new_list.index(num)
    index_list[index].append(i)

filtered_list = [lst for lst in index_list if len(lst) >= 2]
ans_list = []

for _ in filtered_list:
    for i in range(len(_) - 1):
        ans_list.append(_[i + 1] - _[i])

print(min(ans_list) + 1)