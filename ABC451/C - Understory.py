q = int(input())
tree = []

for i in range(q):
    operation, h = map(int, input().split())

    if operation == 1:
        tree.append(h)
        tree.sort()
    else:
        tree.remove(h)
    
    print(len(tree))