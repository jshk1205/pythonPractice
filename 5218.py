for _ in range(int(input())):
    text1, text2 = map(str, input().split())
    result = []
    for i in range(0, len(text1)):
        if ord(text1[i]) <= ord(text2[i]):
            result.append(ord(text2[i])-ord(text1[i]))
        elif ord(text1[i]) > ord(text2[i]):
            result.append((26+ord(text2[i])) - ord(text1[i]))
    print('Distances:', end=' ')
    for k in range(0, len(result)):
        print(result[k],end=' ')
    print()