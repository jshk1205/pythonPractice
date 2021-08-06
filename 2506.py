n = int(input())
count, result = 0, 0
g = list(map(int,input().split()))
for i in range(0, len(g)):
    if g[i] == 1:
        count += 1
        result += count
    else:
        count = 0
print(result)