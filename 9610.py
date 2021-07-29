n = int(input())
q1, q2, q3, q4, axis = 0, 0, 0, 0, 0
for i in range(0, n):
    x, y = map(int, input().split())
    if x == 0 or y == 0:
        axis += 1
    elif x > 0 and y > 0:
        q1 += 1
    elif x > 0 and y < 0:
        q4 += 1
    elif x < 0 and y > 0:
        q2 += 1
    else:
        q3 += 1
print("Q1: "+ str(q1))
print("Q2: "+ str(q2))
print("Q3: "+ str(q3))
print("Q4: "+ str(q4))
print("AXIS: "+ str(axis))