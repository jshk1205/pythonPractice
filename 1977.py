m = int(input())
n = int(input())
result = 0
square = []

for i in range(m, n+1):
    for k in range(1, 101): # m과 n의 최대수가 10000이기 때문에 완전 제곱수의 최대는 100이다
        if i == k * k:
            result += i
            square.append(i)
if result == 0:
    print('-1')
else:
    print(result)
    print(square[0])