a, b = map(int, input().split())
c, d = map(int, input().split())
e, f = map(int, input().split())

if a == c and b != d:
    h = 0
    g = e
    if b > d and f != b:
        h = b
    elif b > d and f == b:
        h = d
    elif d > b and f == d:
        h = b
    else:
        h = d
    print(str(g)+' '+str(h))
elif a == e:
    h = 0
    g = c
    if b > f and d != b:
        h = b
    elif b > f and d == b:
        h = f
    elif f > b and f == d:
        h = b
    else:
        h = f
    print(str(g) + ' ' + str(h))
elif c == e:
    h = 0
    g = a
    if d > f and d != b:
        h = d
    elif d > f and d == b:
        h = f
    elif f > d and f == b:
        h = d
    else:
        h = f
    print(str(g) + ' ' + str(h))