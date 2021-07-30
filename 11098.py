n = int(input())
for _ in range(0, n):
    p = int(input())
    price = []
    name= []
    for _ in range(0, p):
        c, m = map(str,input().split())
        c = int(c)
        price.append(c)
        name.append(m)
        ex = 0
        num =0
        for i in range(0,len(price)):
            if ex < price[i]:
                ex = price[i]
                num = i
    print(name[num])