n = int(input())
num=[]
for i in range(0, n):
    lis = int(input())
    num.append(lis)

for j in sorted(num):
    print(j)