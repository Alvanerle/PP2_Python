import re 

txt = "The rain in Spain 1234"
x = re.search(r"(.+)(\b[0-9]+)", txt)

print(x)
print(x.groups())