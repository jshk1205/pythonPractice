grade = input()
grade =int(grade)
if grade >89 :
    print('A')
elif grade<90 and grade >79:
    print('B')
elif grade<80 and grade > 69:
    print('C')
elif grade<70 and grade > 59:
    print('D')
else:
    print('F')