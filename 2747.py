n = int(input())
num1, num2 = 0, 1
for i in range(0,n):
    next = num1 + num2
    num1 = num2
    num2 = next
print(num1)