import re

txt = "Spain rain drain pain sdasd random words contain"

x = re.findall("\S*ain", txt)

print(x)