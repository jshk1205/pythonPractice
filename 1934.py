n = int(input())
for i in range(0, n):
    a, b = map(int,input().split())
    if a < b: # (a,b)로 연산을 하기 때문에 a가 b 보다 커야 한다다
        temp = a
        a = b
        b = temp
    # 최소 공배수 부분에서 원래 입력받은 a,b 의 값을 사용해야 되기 때문에 다른변수에 저장
    num = a
    num2 = b
    while b != 0:# 최대 공약수 구하는 부분
        r = a % b
        a, b = b, r
    result = (num * num2) // a # 최소 공배수 구하는 부분 (입력받은 두자연수 / 최대공배수)
    print(result)