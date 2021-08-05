#Python3로 할 경우 시간초과 발생 PyPy3로 해야됩니다.
m = int(input())
n = int(input())
decimal = []
for i in range(m, n+1):
    count = 0
    for k in range(1, i+1):
        if i % k == 0:
            count += 1
    if count == 2:
        decimal.append(i)
if len(decimal) > 0:
    print(sum(decimal))
    print(decimal[0])
else:
    print('-1')