s = input()
stack = []
pair = {')': '(', ']': '[', '}': '{'}

for char in s:
    if char in '({[':
        stack.append(char)
    elif char in ')}]':
        # スタックが空 or スタックの最後の要素が対応する括弧でない場合
        if not stack or stack[-1] != pair[char]:
            print('No')
            exit()
        stack.pop()

print('Yes' if not stack else 'No')