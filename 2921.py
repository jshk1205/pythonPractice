n = int(input())
total = 0
for i in range(0,n+1):
    for k in range(i, n+1):
        total += i + k
print(total)