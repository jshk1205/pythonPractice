n = int(input())
for i in range(0, n):
    count = 1
    final = 0
    result = list(map(str,input()))
    for k in range(0, len(result)):
       if result[k] == 'O':
           final += count
           count += 1
       else:
           count = 1
    print(final)