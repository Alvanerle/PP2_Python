cnt = 0
x = 1
while x != 0:
    x = int(input())
    if x % 2 == 0 and x != 0:
        cnt += 1

print(cnt)