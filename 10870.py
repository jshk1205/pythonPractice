n = int(input())
num_list = [0, 1]
for i in range(0, n-1):
    num = num_list[i] + num_list[i+1]
    num_list.append(num)
print(num_list[n])