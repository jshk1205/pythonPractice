n = int(input())
num_list = []
for _ in range(0, n):
    num = int(input())
    num_list.append(num)
num_list = sorted(num_list,reverse= False) #reverse= False 는 default값이다
for i in range(0, n):
    print(num_list[i], end='\n')