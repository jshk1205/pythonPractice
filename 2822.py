score_list = []
smax = []
use_list = []
for _ in range(0, 8):
    score = int(input())
    score_list.append(score)
    score_list_sort = sorted(score_list, reverse= True)
for i in range(0,5):
    smax.append(score_list_sort[i])
    use = score_list.index(smax[i])+1
    use_list.append(use)
use_list = sorted(use_list)
print(sum(smax))
for k in range(0, 5):
    print(use_list[k], end=' ')