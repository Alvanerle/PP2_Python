n = int(input())

cnt = 0

ans = 0
while cnt != n:
    cnt += 1
    if(cnt == n):
        ans += 45
        continue
    if cnt % 2 == 1:
        ans += 50
    else:
        ans += 60

h = int(ans / 60) + 9
m = ans % 60

print(str(h) + ' ' + str(m))