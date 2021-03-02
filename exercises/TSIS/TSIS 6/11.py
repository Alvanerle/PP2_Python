x = int(input())

total = 0
for i in range(1, int(x / 2) + 1):
    if x % i == 0:
        total += i
    
if total == x:
    print('Yes')
else:
    print('No')