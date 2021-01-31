n = int(input())

s1 = "+___ "
s2 = "|{} / "
s3 = "|__\ "
s4 = "|    "

ss1 = ""
ss2 = ""
ss3 = ""
ss4 = ""

for i in range(1, n + 1):
    ss1 += s1
    ss2 += s2.format(i)
    ss3 += s3
    ss4 += s4

print(ss1)
print(ss2)
print(ss3)
print(ss4)

