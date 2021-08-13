s= str(input())
s_list = list(s)
alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphabet_list = list(alphabet)
use_list = [-1 for i in range(26)]
for i in range(0, len(s_list)):
    for k in range(0, len(alphabet_list)):
        if s_list[i] == alphabet_list[k]:
            if use_list[k] == -1:
                use_list[k]=i
for j in range(0, len(use_list)):
    print(use_list[j], end=' ')