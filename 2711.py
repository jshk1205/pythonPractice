t = int(input())
text_list = []
for _ in range(0, t):
    position, text = map(str, input().split())
    position = int(position) -1
    text_list = list(text)
    del text_list[position]
    for i in range(0, len(text_list)):
        print(text_list[i], end='')
    print()