n = int(input())

a = []
ans = 0
for i in range(n):
    a.append(int(input()))
    ans += a[i]

print(ans)