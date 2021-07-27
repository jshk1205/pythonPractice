n = int(input())
num = 2
while n != 1:
    if n % num == 0:
        n = n/num
        print(num)
    else:
        num += 1
