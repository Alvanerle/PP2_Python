f = open("demofile.txt", "r")
f.seek(4)
print(f.readline())