from string import ascii_uppercase
from string import ascii_lowercase
text = str(input())
alphabet_low = list(ascii_lowercase)
alphabet_upp = list(ascii_uppercase)
ROT13 = []
for i in text:
    if i.isupper() == True: #대문자인 경우
        position = (alphabet_upp.index(i) + 13) % 26
        ROT13.append(alphabet_upp[position])
    elif i.islower() == True: # 소문자인 경우
        position = (alphabet_low.index(i) + 13) % 26
        ROT13.append(alphabet_low[position])
    elif i == ' ':
        ROT13.append(i)
    else:
        ROT13.append(i)
for k in range(0, len(ROT13)):
    print(ROT13[k], end='')