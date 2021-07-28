k, n, m = map(int, input().split())# 과자 한개 가격 k, 과자의 개수 n, 동수가 가진 돈m
result = (k * n) - m
if result < 0:
    result = 0
print(result)