text = list(str(input()))
for i in range(0, len(text)):
    if text[i].isupper() == True:
        text[i] = text[i].lower()
    else:
        text[i] = text[i].upper()
for i in range(0, len(text)):
    print(text[i],end='')
