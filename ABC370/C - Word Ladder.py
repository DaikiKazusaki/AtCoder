s = list(input())
t = list(input())
x = list()

sorted_t = sorted(t)

print(sorted_t)

for item in sorted_t:
    index = t.index(item)
    if s[index] != item:
        x.append(s)
    
print(x)