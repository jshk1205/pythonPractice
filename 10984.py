t1 = int(input()) # 학기 수
for _ in range(0, t1):
    t2 = int(input())  # 과목 수
    totalC = 0
    totalG = 0
    gpa = 0
    for _ in range(0, t2):
        c, g = map(float,input().split())
        totalC += c
        totalG += g * c
    gpa = totalG / totalC
    print(int(totalC), '%.1f' % gpa )