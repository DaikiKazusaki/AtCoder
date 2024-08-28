from string import ascii_lowercase

n = int(input())
s = list(input())
q = int(input())

char_from = ascii_lowercase
char_to = ascii_lowercase

for _ in range(q):
    c, d = input().split()
    char_to = char_to.replace(c, d)

