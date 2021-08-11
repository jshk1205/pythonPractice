k = int(input())
num_list = []
for _ in range(0, k):
    num = int(input())
    if num == 0:
        num_list.pop()
    else:
        num_list.append(num)
print(sum(num_list))
