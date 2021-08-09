grade_list = []
for _ in range(5):
    g1,g2,g3,g4 = map(int, input().split())
    score = g1+g2+g3+g4
    grade_list.append(score)
gmax = 0
position = 0
for i in range(0, len(grade_list)):
    if gmax < grade_list[i]:
        gmax = grade_list[i]
        position = i + 1
print(position, max(grade_list))