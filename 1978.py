n= int(input()) # 리스트 원소 개수 입력
num = list(map(int, input().split(' '))) # 리스트 원소 입력
dec = 0 #소수의 개수

if n == len(num): # 지정한 리스트의 원소 개수와 입력한 리스트의 원소의 수가 같은경우 실행
    for i in num:
        count = 0  # 약수의 개수
        for k in range(1, i+1): #약수의 개수 구하기
            if i % k == 0:
                count += 1
        if count == 2: # 약수의 개수가 2이면 소수개수 1증가
            dec += 1
print(dec)

#지정한 리스트의 원소의 개수와 입력한 리스트원소의 수가 달라고 지정한 원소의 개수 만큼만 실행
# lis=[] # 원소 개수 만큼 담을 리스트
# if n < len(num): # 입력 받은 리스트의 원소 개수 만큼 lis에 담는다
#     for i in range(0,n):
#         lis.append(num[i])
#
# else: # 입력 받은 원소를 lis에 입력
#     for i in range(0,n):
#         lis.append(num[i])
#         lis[i]= int(lis[i])
# print(lis)

