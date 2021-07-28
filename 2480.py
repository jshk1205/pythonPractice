a, b, c = map(int, input().split())
if a == b and a == c and b == c:
    result = 10000 + (a * 1000)
elif a == b or a == c and b != c:
    result = 1000 +(a * 100)
elif b == c or b == a and a != c:
    result = 1000 + (b * 100)
elif c == a or c == b and a != b:
    result = 1000 + (c * 100)
elif a != b and a != c and b != c:
    num = 0
    if a > b and a> c:
        num = a
    elif b > a and b > c:
        num = b
    else :
        num = c
    result = num * 100
print(result)