import math

pi = 0
i = 1
while i <= 10:
    pi += 1 / (i * i)
    i += 1

pi = math.sqrt(pi * 6)

print(pi)