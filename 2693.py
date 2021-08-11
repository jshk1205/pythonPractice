t = int(input())
for _ in range(0, t):
    numA_list = list(map(int,input().split()))
    numA_list.sort()
    print(numA_list[-3])