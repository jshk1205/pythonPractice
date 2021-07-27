a, b, c = map(int, input().split()) # a -> 시 b -> 분 c -> 초
d = int(input())
while d != 0:
    if c + d >59:
        d = d - (60 - c)
        c = 0
        b += 1
    else:
        c += d
        d = 0
    if b > 59 :
        a += 1
        b = 0
    if a > 23:
        a = 0
print(str(a) + ' '+ str(b)+ ' '+ str(c))