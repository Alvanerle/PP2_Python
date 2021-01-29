n = int(input())

h = str(int(n / 3600) % 24)
mm = str(int((n / 60) % 60 / 10)) + str(int((n / 60) % 60 % 10))
ss = str(int((n % 60) / 10)) + str((n % 60) % 10)

print(h + ":" + mm + ":" + ss)