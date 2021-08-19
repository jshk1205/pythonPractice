longname = list(str(input()))
print(longname[0],end='')
for i in range(0, len(longname)):
    if longname[i] == '-':
        print(longname[i+1],end='')