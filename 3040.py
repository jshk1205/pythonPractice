height_list = []
for _ in range(0, 9):
    height = int(input())
    height_list.append(height)
total = sum(height_list)
ex1, ex2 = 0, 0
for i in range(0, len(height_list)):
    for k in range(i+1, len(height_list)):
        if total - (height_list[i]+height_list[k]) == 100:
            ex1 = height_list[i]
            ex2 = height_list[k]
height_list.remove(ex1)
height_list.remove(ex2)
for j in range(0, len(height_list)):
    print(height_list[j], end='\n')
