d = list(input())

for _ in d:
    if _ == "N":
        print("S", end="")
    elif _ == "S":
        print("N", end="")
    elif _ == "W":
        print("E", end="")
    elif _ == "E":
        print("W", end="")
