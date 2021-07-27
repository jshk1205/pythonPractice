A = int(input())
oper = str(input())
B = int(input())
if A % 10 == 0 or A == 1:
    if B % 10 == 0 or B == 1:
        if oper == '+':
            result = A + B
        elif oper == '*':
            result = A * B
        print(result)