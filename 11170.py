for _ in range(0, int(input())):
    n, m = map(int, input().split())
    count = 0
    for i in range(n, m+1):
        i = list(str(i))
        for k in range(0, len(i)):
            if i[k] == '0':
                count += 1
    print(count)