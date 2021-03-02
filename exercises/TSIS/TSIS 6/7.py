def count(s):
    a = [0, 0]
    for x in s:    
        if ord(x) >= ord('a') and ord(x) <= ord('z'):
            a[0] += 1
        elif x != ' ':
            a[1] += 1
    return a

s = input()

print('Number uppercase letters: {}\nNumber of lower case letters: {}'.format(count(s)[1], count(s)[0]))