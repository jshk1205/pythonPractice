num1, num2, num3, num4, num5 = map(int,input().split())
num1 = num1*num1
num2 = num2*num2
num3 = num3*num3
num4 = num4*num4
num5 = num5*num5
total = num1 + num2 + num3 + num4 + num5
result = total % 10
print(result)