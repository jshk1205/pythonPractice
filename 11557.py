t = int(input())
for i in range(0, t):
    n = int(input())
    school = []
    drink = []
    for j in range(0, n):
        s, l = map(str, input().split())
        l = int(l)
        school.append(s)
        drink.append(l)
        big = 0
    for k in range(0, len(drink)):
        if drink[k] > big:
            big = drink[k]
    for g in range(0, len(drink)):
        if big == drink[g]:
            print(school[g])