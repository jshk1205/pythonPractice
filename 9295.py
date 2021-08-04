import sys
t = int(input())
for i in range(0,t):
    num1, num2 = map(int, sys.stdin.readline().split())
    total = num1 + num2
    print('Case',str(i+1)+':',total)