num1, num2 = map(int, input().split())
if num1 < num2:
    temp = num1
    num1 = num2
    num2 = temp
a, b = num1, num2
while num2 != 0:
    r= num1 % num2
    num1, num2 = num2, r
    factor = num1
    multi = (a * b) // num1
print(factor) #최대공약수
print(multi) # 최소공배수