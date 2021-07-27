t = int(input())
for i in range(0, t):
    text = list(map(str, input().split()))
    result = []
    mul = int(text[0])
    temp = list(text[1])
    for k in range(0, len(temp)):
        for j in range(0, mul):
            result.append(temp[k])
    print(''.join(result))