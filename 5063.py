n = int(input())
for i in range(0, n):
    r, e, c = list(map(int, input().split()))
    price = e - c
    if r < price:
        print('advertise')
    elif r == price:
        print('does not matter')
    elif r > price:
        print('do not advertise')