import re 

s = input()

pattern = re.compile(r"[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm]{1}[AEIOUaeiou]{1}[AEIOUaeiou]+[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm]{1}")
matches = pattern.finditer(s)

ok = False
for match in matches:
    x = str(match.group(0))
    for i in range(1, len(x) - 1):
        print(x[i], end = '')
        ok = True
    print()
if ok == False:
    print(-1)