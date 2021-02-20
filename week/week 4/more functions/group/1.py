#.group() returns the part of the 
#string where there was a match

import re

txt = "The rain in Spain Srain Sfdfd"
x = re.search(r"\bS\w+", txt)

print(x.group())