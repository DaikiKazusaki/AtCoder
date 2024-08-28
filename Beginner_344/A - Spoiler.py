def remove_between_bars(S):
    start = S.find('|')
    end = S.rfind('|')
    return S[:start] + S[end+1:]

# テスト
S = input()
print(remove_between_bars(S))
