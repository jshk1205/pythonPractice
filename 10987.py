text = list(str(input()))
count = 0
for i in range(0, len(text)):
    if text[i] == 'a' or text[i] == 'e' or text[i] == 'i' or text[i] == 'o' or text[i] == 'u':
        count += 1
print(count)