h, w = map(int, input().split())
si, sj = map(int, input().split())
si -= 1
sj -= 1
c = []
for i in range(h):
    c.append(list(input().strip()))
x = list(input())

for item in x:
    ni, nj = si, sj
    if item == 'L':
        nj -= 1
    elif item == 'R':
        nj += 1
    elif item == 'U':
        ni -= 1
    elif item == 'D':
        ni += 1
    
    if 0 <= ni < h and 0 <= nj < w and c[ni][nj] == '.':
        si, sj = ni, nj

print(si + 1, sj + 1)