num_list = []
for _ in range(0, 5):
    num = int(input())
    num_list.append(num)
ave = sum(num_list) // 5
num_list = sorted(num_list)
print(ave)
print(num_list[2])