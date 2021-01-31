a = []

ans = 0
for i in range(10):
    a.append(int(input()))
    ans += a[i]

print(ans)