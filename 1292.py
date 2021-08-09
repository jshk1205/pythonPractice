a, b = map(int, input().split())
num_list = []
for i in range(1, b+1):
    for k in range(0, i):
        num_list.append(i)
sum = 0
for j in range(a, b+1):
    sum += num_list[j-1]
print(sum)