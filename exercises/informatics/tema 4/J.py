x = int(input())

ans = 0
for i in range(1, x):
    if i + 1 == x:
        ans += i * (i + 1)
        print("{}*{}={}".format(i, i + 1, ans))
    else:
        ans += i * (i + 1)
        print("{}*{}+".format(i, i + 1), end = "")

