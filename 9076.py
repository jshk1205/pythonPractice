t = int(input())
for _ in range(0, t):
    grade = list(map(int,input().split()))
    grade.remove(max(grade))
    grade.remove(min(grade))
    if max(grade) - min(grade) >= 4:
        print('KIN')
    else:
        print(sum(grade))