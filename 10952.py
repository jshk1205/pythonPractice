while True:
    numA, numB = map(int, input().split())
    if numA == 0 and numB == 0:
        break
    else:
        print(numA + numB)