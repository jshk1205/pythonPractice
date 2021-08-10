num = list(map(int,input()))
num = sorted(num, reverse=True)
for i in range(0,len(num)):
    print(num[i],end='')