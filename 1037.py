n = int(input())
num = list(map(int,input().split()))
if n == len(num):
    result = max(num) * min(num)
    print(result)