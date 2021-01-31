n = int(input())

mx = ""
mn = "1"
for i in range(0, n):
    mx += "9"
    if i < n - 1:
        mn += "0"

mx = int(mx)
mn = int(mn)

for i in range(mx, mn - 1, -2):
    print(i)
