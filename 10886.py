n = int(input())
temp = []
cute = 0
ncute = 0
for i in range(0,n):
    ticket = str(input())
    temp.append(ticket)
for k in range(0, len(temp)):
    if temp[k] == '1':
        cute += 1
    else :
        ncute +=1
if cute > ncute:
    print("Junhee is cute!")
elif ncute > cute:
    print("Junhee is not cute!")