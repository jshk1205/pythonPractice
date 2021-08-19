from string import ascii_uppercase
alphabet = list(ascii_uppercase)
text = list(str(input()))
for i in range(0, len(text)):
    text[i] = text[i].upper()
use_case = [0 for i in range(26)]
for i in range(0, len(text)):
    for k in range(0, len(alphabet)):
        if text[i] == alphabet[k]:
            use_case[k] += 1
max_text = max(use_case)
position = use_case.index(max_text)
use_case.remove(max_text)
if max_text in use_case:
    print('?')
else:
    print(alphabet[position])