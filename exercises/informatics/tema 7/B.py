import math

n = int(input())

t = int(math.sqrt(n))
ok = False
for i in range(2, t + 1):
    if n % i == 0:
        ok = True
        print(i)
if ok == False:
    print(n)