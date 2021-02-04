a = float(input())

h = (12 * a) / 360
m = (h - int(h)) * 60
s = (m - int(m)) * 60

print(str(int(h)) + " " + str(int(m)) + " " + str(int(s)))