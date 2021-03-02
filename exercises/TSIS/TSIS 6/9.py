import math

def prime(x):
    i = 2
    while i * i <= x:
        if x % i == 0:
            return False
        i += 1
    if x == 1:
        return False 
    else:
        return True

x = int(input())

if prime(x):
    print('YES')
else:
    print('NO')