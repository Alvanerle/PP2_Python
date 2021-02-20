#The sub() function replaces the 
#matches with the text of your choice:

import re

txt = "Salam Hello Hi Privet"

x = re.sub("\s", ",", txt)

print(x)