a =int(input())
b =int(input())
c =int(input())
mul = a * b* c
count = [0,0,0,0,0,0,0,0,0,0]
while mul != 0:
    position = mul % 10
    count[position] += 1
    mul = mul //10
for i in range(0,len(count)):
    print(count[i])