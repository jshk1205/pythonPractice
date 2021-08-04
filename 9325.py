case = int(input())
for _ in range(0, case):
    s = int(input())
    n = int(input())
    temp = 0
    for i in range(0,n):
        q, p = map(int,input().split()) # q: 옵션개수 p: 옵션가격
        temp += q * p
    result = s + temp
    print(result)