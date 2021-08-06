day = int(input())
count = 0
car = list(map(int, input().split()))
for i in range(0, len(car)):
    if day == car[i]:
        count += 1
print(count)