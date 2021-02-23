import re 

s = input()

pattern = re.compile(r"[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm]{1}([AEIOUaeiou]{1}[AEIOUaeiou]+)[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm]{1}")
find = re.search(pattern, s)

if not find:
    print(-1)
else:
    while find:
        print(find.group(1))
        find = pattern.search(s, find.start() + 1)