n, x = map(int,input().split())
m = list(map(int, input().split()))
for i in range(0,n):
    if x > m[i]:
        print(m[i],end=' ')