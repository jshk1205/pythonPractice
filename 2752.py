num_list = list(map(int, input().split()))
num_list = sorted(num_list)
for i in range(0,len(num_list)):
    print(num_list[i], end =' ')