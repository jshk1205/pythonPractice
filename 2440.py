n = int(input())
for i in range(n+1,1,-1):
    for k in range(i,1,-1):
        print('*',end='')
    print(end='\n')