n = int(input())
final =0
result1, result2, result3 =0, 0, 0
while n > 0:
    a, b, c = map(int, input().split())
    if a == b and a == c and b == c:
        result1 = 10000 + (a * 1000)
    elif a == b or a == c and b != c:
        result2 = 1000 +(a * 100)
    elif b == c or b == a and a != c:
        result2 = 1000 + (b * 100)
    elif c == a or c == b and a != b:
        result2 = 1000 + (c * 100)
    elif a != b and a != c and b != c:
        num = 0
        if a > b and a> c:
            num = a
        elif b > a and b > c:
            num = b
        else :
            num = c
        result3 = num * 100
    if result1 >= result2 and result1 >= result3 and result1 > final:
        final = result1
    elif result2 >= result1 and result2 >= result3 and result2 > final:
        final = result2
    elif result3 >= result1 and result3 >= result2 and result3 > final:
        final = result3
    n -= 1

print(final)
