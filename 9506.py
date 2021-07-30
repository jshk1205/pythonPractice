while True:
    n = int(input())
    if n == -1:
        break
    else:
        num = 0
        numlis = []
        for i in range(1, n):
            if n % i == 0:
                num += i
                numlis.append(i)
        if n == num:
            print(str(n) + ' =', end=' ')
            print(str(numlis[0]), end=' ')
            for k in range(1, len(numlis)):
                if numlis[len(numlis)-1] == numlis[k]:
                    print('+ '+ str(numlis[k]))
                else:
                    print('+ '+ str(numlis[k]),end=' ')
        else:
            print(str(n) +' is NOT perfect.')
