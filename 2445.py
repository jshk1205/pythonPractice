n = int(input())
for i in range(1,n+1):
    print('*'*i+' '*(n-i),end='')
    print(' '*(n-i) + '*'*i)
for k in range(1, n):
    print('*'*(n-k)+' '*k,end='')
    print(' ' * k + '*' * (n - k))