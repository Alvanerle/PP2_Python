cnt = 0
sum = 0
x = 1
while x != 0:
    x = int(input())
    cnt += 1
    sum += x

print(sum / (cnt - 1))