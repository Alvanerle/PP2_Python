x = input()

ind = 0
for i in range(len(x)):
    if(x[i] == '.'):
        ind = i + 1
        break

print("0.", end = "")
if ind != 0:
    for i in range(ind, len(x)):
        print(x[i], end = "")
else:
    print(0)

# x = float(input())
# print(x - int(x))