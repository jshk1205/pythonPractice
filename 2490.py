for _ in range(0,3):
    count = 0
    num = list(map(int,input().split()))
    for i in range(0,4):
        if num[i] == 1:
            count += 1
    if count == 3:
        print('A')
    elif count == 2:
        print('B')
    elif count == 1:
        print('C')
    elif count == 0:
        print('D')
    else:
        print('E')