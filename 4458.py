for _ in range(0, int(input())):
    text = list(str(input()))
    first = text.pop(0)
    if first.isupper() == False:
        first=first.upper()
    print(first ,end='')
    for i in range(0, len(text)):
        print(text[i],end='')
    print()