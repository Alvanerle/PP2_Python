f1 = open('input.txt', 'r')
f2 = open('abc.txt', 'a')

f2.write(f1.read())
f2.close()
f2 = open('abc.txt', 'r')
print(f2.read())