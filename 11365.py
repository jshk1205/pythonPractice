while True:
    text = str(input())
    if text == 'END':
        break
    text = list(text)
    for i in range(len(text)-1, -1, -1):
        print(text[i], end='')
    print()