t = int(input())
for i in range(0,t):
    num = list(map(str, input().split()))
    result = 0
    for k in range(0, len(num)):
        if k == 0 :
            result += float(num[k])
        else:
            if num[k] == '@':
                result *= 3
            elif num[k] == '%':
                result += 5
            elif num[k] =='#':
                result -= 7
    print(format(result, ".2f"))
