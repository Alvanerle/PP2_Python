a = list(map(int, input().split()))

ans = 10000
for num in a:
    if num > 0:
        ans = min(ans, num)

print(ans)