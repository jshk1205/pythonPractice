n = int(input())
for i in range(0,n):
    print(' '*i + '*'*(n-i), end='')
    print('*'*((n-i)-1))
for k in range(2, n+1):
    print(' '* (n - k) + '*'*k,end='')
    print('*'*(k-1))