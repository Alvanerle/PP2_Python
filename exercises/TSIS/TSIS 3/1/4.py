a = list(map(int, input().split()))

cnt = 0

for num in a:
    if num != 0:
        print(num, end = " ")
    else:
        cnt += 1
    
for i in range(cnt):
    print(0, end = " ")

