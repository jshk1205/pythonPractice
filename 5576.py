w_list = []
k_list = []
for i in range(0,20):
    if i < 10:
        w = int(input())
        w_list.append(w)
    if i > 9:
        k = int(input())
        k_list.append(k)
w_list = sorted(w_list,reverse=True)
k_list = sorted(k_list,reverse=True)
w_top = []
k_top = []
for i in range(0, 3):
    w_top.append(w_list[i])
    k_top.append(k_list[i])
print(sum(w_top),sum(k_top))
