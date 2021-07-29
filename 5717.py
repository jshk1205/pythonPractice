while True:
    m, f =map(int, input().split())
    if m < 6 and f < 6 and m > 0 and f > 0:
        print(m+f)
    elif m == 0 and f == 0 :
        break
