a, b, c = map(int,input().split())
result = 0
if a >= b and a <= c:
		result = a
elif a >= c and a <= b:
	result= a
elif b >= a and b <= c:
    result = b
elif b >= c and b <= a:
    result = b
else:
    result = c
print(result)
