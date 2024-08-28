q = int(input())
num_list = []
ans_list = []

for i in range(q):
    a, b = map(int, input().split())
    if a == 1:
        num_list.append(b)
    elif a == 2:
        ans_list.append(num_list[len(num_list) - b])

for i in range(len(ans_list)):
    print(ans_list[i])