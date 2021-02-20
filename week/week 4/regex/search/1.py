import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

if x:
    print("found")
else:
    print("not found")