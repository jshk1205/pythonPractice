n = int(input())
num=[]
for i in range(0, n):
    lis = int(input())
    num.append(lis)
    num.sort()
for j in range(0, n):
    print(num[j], end="\n")