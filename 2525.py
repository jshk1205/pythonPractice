A, B = map(int, input().split())
C = int(input())
while C >= 0:
    if B + C > 59:
        A += 1
        C =C - (60 - B)
        B = 0
    else:
        B += C
        C = 0
    if A > 23:
        A = 0
    if C == 0:
        break
print(str(A) + " "+ str(B))