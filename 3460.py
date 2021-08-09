t = int(input())
for _ in range(0, t):
    binary = []
    n = int(input())
    while n > 0:
        num = n % 2
        binary.append(num)
        n = n // 2
    for k in range(0, len(binary)):
        if binary[k] == 1:
            print(k,end=' ')
