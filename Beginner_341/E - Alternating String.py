n, q = map(int, input().split())
s = list(input())
query = [list(map(int, input().split())) for _ in range(q)]

for _ in range(q):
    choice = query[_][0]
    left = query[_][1]
    right = query[_][2]

    if choice == 1:
        for i in range(left - 1, right - 1):
            if s[i] == "0":
                s[i] = "1"
            else:
                s[i] = "0"
    else:
        if all(s[i] != s[i + 1] for i in range(left - 1, right - 2)):
            print("YES")
        else:
            print("NO")