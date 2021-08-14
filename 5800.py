k = int(input())
for i in range(0, k):
    grade = list(map(int, input().split()))
    del grade[0]
    print('Class',i+1)
    grade = sorted(grade,reverse=True)
    grap = 0
    for j in range(0, len(grade)-1):
        if grade[j] - grade[j+1] > grap:
            grap = grade[j] - grade[j+1]
    print('Max',max(grade), end='')
    print(', '+'Min', min(grade),end='')
    print(', '+'Largest gap', grap)