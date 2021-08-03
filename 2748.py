n = int(input())
f1, f2 = 0, 1
result = 0
for i in range(0, n):
    result = f1 + f2
    f2 = f1
    f1 = result
print(result)