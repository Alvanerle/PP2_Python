pi = 0

i = 1
tmp = 1
while i <= 10:
    if i % 2 == 1:
        pi += 4 / tmp
    else:
        pi -= 4 / tmp
    i += 1
    tmp += 2

print(pi)