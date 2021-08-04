import sys
t = int(input())
for _ in range(0,t):
    v, e = map(int, sys.stdin.readline().split()) # v 꼭짓점 개수 e 모서리개수
    side = 2 - v + e
    print(side)