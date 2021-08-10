hight_list = []
for _ in range(0, 9):
    hight = int(input())
    hight_list.append(hight)
hight_list = sorted(hight_list)
total = sum(hight_list)
del1, del2 = 0, 0
for i in range(0, 9):
    for k in range(i+1, 9):
        if total - (hight_list[i] + hight_list [k]) == 100:
            del1 = hight_list[i]
            del2 = hight_list[k]
hight_list.remove(del1)
hight_list.remove(del2)
for j in range(0, len(hight_list)):
    print(hight_list[j])