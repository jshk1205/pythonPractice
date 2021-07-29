text = list(map(str,input()))
count =0
for i in range(0, len(text)-1):
    temp = len(text)-1 - i
    if text[i] == text[temp]:
        count += 0
    else:
        count += 1
if count == 0:
    print('1')
else:
    print('0')