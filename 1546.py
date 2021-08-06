n = int(input())
score = list(map(int,input().split()))
high = max(score)
low,average = 0, 0
grade = []
for i in range(0, len(score)):
    low = (score[i]/high) * 100
    grade.append(low)
average = sum(grade) /n
print(average)