x = int(input())

a = "The next number for the number {} is {}."
b = "The previous number for the number {} is {}."

print(a.format(x, x + 1))
print(b.format(x, x - 1))
