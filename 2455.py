temp = 0
total = []
for _ in range(0, 4):
    n, m = map(int,input().split())#n 내린사람 m 탄사람
    temp += m
    temp -= n
    total.append(temp)
print(max(total))