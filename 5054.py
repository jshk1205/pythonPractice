t= int(input())
for _ in range(0, t):
    n = int(input()) # 상점의 수
    location = list(map(int,input().split()))
    location = sorted(location)
    print((location[-1]-location[0])*2)
