v = int(input())
aCount = 0 # 성적 A의 개수
bCount = 0 # 성적 B의 개수
# for k in range(0,v):
grade = list(map(str,input()))
for i in range(0, len(grade)):
    if grade[i] == 'A':
        aCount += 1
    elif grade[i] == 'B':
        bCount +=1
if aCount > bCount:
    print('A')
elif bCount > aCount:
    print('B')
else:
    print('Tie')