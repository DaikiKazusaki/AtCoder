n = int(input())
a = list(map(int, input().split()))
count = 0

while True:
    a.sort(reverse = True)
    
    if a[0] == 0 or a[1] == 0:
        break

    a[0] -= 1
    a[1] -= 1
    count += 1

print(count)