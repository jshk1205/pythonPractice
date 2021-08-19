n = str(input())
text = 0
if len(n) %10 != 0:
    text = (len(n)//10) +1
else:
    text = len(n)//10
for i in range(1, text+1):
    print(n[10*(i-1):10*i])