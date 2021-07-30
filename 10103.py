n = int(input())
cgrade = 100
sgrade = 100
for i in range(0,n):
    chang, sang = map(int, input().split())
    if chang > sang:
        sgrade -= chang
    elif chang < sang:
        cgrade -= sang

print(cgrade)
print(sgrade)