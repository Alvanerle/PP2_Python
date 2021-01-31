x = input()

ind = 0
for i in range(len(x)):
    if(x[i] == '.'):
        ind = i + 1
        break

if ind != 0:
    print(x[ind])    
else:
    print(0)

# x = float(input())
# print(int(x * 10) % 10)