x, y = map(str, input().split())
x = int(x[::-1])
y = int(y[::-1])
xy = str(x + y)
print(int(xy[::-1]))
