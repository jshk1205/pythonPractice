from string import ascii_lowercase
s = list(str(input()))
alphabet = list(ascii_lowercase)
use_case = [0 for i in range(26)]
for i in range(0, len(s)):
    for k in range(0, len(alphabet)):
        if s[i] == alphabet[k]:
            use_case[k] += 1
for j in range(0, len(use_case)):
    print(use_case[j], end=' ')