n = int(input())
x = float(input())

ans = 1

tmp = 1
for i in range(1, n + 1):
    ans += x * tmp
    tmp *= x
print(ans)