a, b = map(int,input().split())
num1 = a // 100 #백의 자리
num2 = (a % 100)//10 #십의 자리
num3 = a % 10 # 일의자리
anum = (num3 *100) + (num2*10) + num1
num1 = b // 100 #백의 자리
num2 = (b % 100)//10 #십의 자리
num3 = b % 10 # 일의자리
bnum = (num3 *100) + (num2*10) + num1
if anum > bnum:
    print(anum)
elif anum < bnum:
    print(bnum)