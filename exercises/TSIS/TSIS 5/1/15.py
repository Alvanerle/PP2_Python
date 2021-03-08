f = open('input.txt', 'r')
l = f.readlines()

line = int(input())
print(l[line - 1], end = '')