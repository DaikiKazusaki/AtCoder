s = input()
not_found = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

for c in s:
    if c in not_found:
        not_found.remove(c)

print(not_found[0])