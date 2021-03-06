s = input()

f = open('text.txt', 'a')
f.write(s)
f.close()

f = open('text.txt', 'r')
print(f.read())