case = int(input())
while case > 0:
    yscore = 0
    kscore = 0
    for i in range(0, 9):
        y, k = map(int, input().split())
        if y > 0 or k > 0:
            yscore += y
            kscore += k
    if yscore > kscore:
        print('Yonsei')
    elif yscore < kscore:
        print('Korea')
    else :
        print('Draw')
    case -= 1