bowl = list(map(str,input()))
height = 10
for i in range(1, len(bowl)):
    if bowl[i-1] == bowl[i]:
        height += 5
    elif bowl[i-1] != bowl[i]:
        height +=10
print(height)