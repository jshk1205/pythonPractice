import sys
case = int(input())
for _ in range(0, case):
    give = 0
    num = 0
    c, v = map(int, sys.stdin.readline().split())
    give = c // v
    num = c % v
    print('You get',give, 'piece(s) and your dad gets',num, 'piece(s).')