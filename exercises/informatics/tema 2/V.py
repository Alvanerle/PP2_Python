n = int(input())
k = int(input())

if(k % n == 0):
    print(0)
    exit(0)

print(n - k % n)
