n = int(input())
s = list(input())

dp = [0, 0, 0]
rock, scissors, paper = dp

for c in s:
    dp = [max(scissors, paper), max(rock, paper), max(rock, scissors)]
    rock, scissors, paper = dp
    if c == 'R':
        scissors = 0
        paper += 1
    elif c == 'S':
        paper = 0
        rock += 1
    elif c == 'P':
        rock = 0
        scissors += 1

print(max(dp))
