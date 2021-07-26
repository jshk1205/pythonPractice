num1 = int(input())
num2 = int(input())
temp1 = num2 % 10 # 일의 자리
temp2 = (num2 %100) // 10 # 십의 자리
temp3 = num2 // 100 #백의 자리
print(num1 * temp1)
print(num1 * temp2)
print(num1 * temp3)
print((num1 * temp1) + (num1 * temp2 *10)+(num1 * temp3*100))