x = float(input())

print(str(int(x)) + " " + str(int((x - int(x)) * 10) + int((x - int(x)) * 100) % 10))