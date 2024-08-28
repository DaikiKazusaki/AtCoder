a = []

while True:
    x = input()
    a.append(x)
    if x == '0':
        break

for i in range(len(a)):
    print(a[len(a)- i - 1])