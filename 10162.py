t = int(input())
a = 300
b = 60
c = 10
aCount, bCount, cCount = 0, 0, 0
while t > 0:
    if t >= a:
        t -= a
        aCount += 1
    elif t < a and t >= b:
        t -= b
        bCount += 1
    elif t < b and t >= c:
        t -= c
        cCount += 1
    elif t < c:
        break
if t == 0:
    print(str(aCount) + ' ' + str(bCount) + ' ' + str(cCount))
else :
    print('-1')