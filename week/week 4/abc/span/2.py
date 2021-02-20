#.span() returns a tuple containing the start-, 
#and end positions of the match.

import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)

print(x.span())