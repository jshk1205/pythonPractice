import sys

n = int(input())
total = []
max = 1
for _ in range(0,n):
    count = int(sys.stdin.readline())
    total.append(count)
for i in range(0, len(total)):
    max += total[i]-1
print(max)