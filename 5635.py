n = int(input())
names = []
birth = []
minPoint, maxPoint = 0, 0
for _ in range(0, n):
    name, day, month, year = map(str,input().split())
    names.append(name)
    if int(month) < 10:
        month = '0'+str(month)
    if int(day) < 10:
        day = '0'+str(day)
    birth.append(year+month+day)
min = int(birth[0])
max = int(birth[0])
for i in range(0,n):
    birth[i] = int(birth[i])
    if birth[i] < min:
        min = birth[i]
        minPoint = i
    if birth[i] > max:
        max = birth[i]
        maxPoint = i

print(names[maxPoint])
print(names[minPoint])