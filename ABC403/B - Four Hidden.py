t = input()
u = input()

for i in range(len(t) - len(u) + 1):
    ok = True
    for j in range(len(u)):
        if t[i + j] != "?" and t[i + j] != u[j]:
            ok = False
            break
    if ok:
        print("Yes")
        exit()

print("No")