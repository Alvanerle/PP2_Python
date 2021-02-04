x = float(input())

n = int(x * 10) % 10

if n < 5:
    print(int(x))
else:
    print(int(x + 0.9))

