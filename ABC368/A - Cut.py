n, k = map(int, input().split())
a = list(map(int, input().split()))

print(*a[-k::] + a[0:-k])