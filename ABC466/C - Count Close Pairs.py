n = int(input())

count = 0
left = 1
right = 2

while right <= n:
    print(f"? {left} {right}", flush=True)
    result = input().strip()
    
    if result == "Yes":
        right += 1
    else:
        count += right - left - 1
        left += 1
        if left == right:
            right += 1

while left < n:
    count += right - left - 1
    left += 1

print(f"! {count}", flush=True)