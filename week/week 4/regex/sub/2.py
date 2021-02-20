#You can control the number of replacements 
#by specifying the count parameter:

import re

txt = "Salam Hello Hi Privet"

x = re.sub("\s", ",", txt, 2)

print(x)