#You can control the number of occurrences 
#by specifying the maxsplit parameter:

import re

txt = "The rain in Spain"
x = re.split("\s", txt, 1)

print(x)