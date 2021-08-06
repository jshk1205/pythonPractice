num =[]
for _ in range(0,7):
    n = int(input())
    num.append(n)
sum = 0
min_list = []
for i in range(0, len(num)):
    if num[i] % 2 !=0:
        sum += num[i]
        min_list.append(num[i])
if len(min_list) > 0:
    print(sum)
    print(min(min_list))
else:
    print('-1')