def fact(x):
    res = 1
    for i in range(1, x + 1):
        res *= i
    return res

x = int(input())
print(fact(x))