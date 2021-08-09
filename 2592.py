num_list = []
for _ in range(0, 10):
    num = int(input())
    num_list.append(num)
ave = 0
most = {}
for i in range(0, len(num_list)):
    ave = num_list[i]+ave
print(ave//10)
for k in num_list: # 딕셔너리 생성
    try: most[k]+=1
    except: most[k]=1
values = most.values() #딕셔너리의 값만 받음
mostnum = max(values) # 딕셔너리의 가장 큰 값 저장
for key, value in most.items(): #가장 큰 값을 이용하여 키값을 출력
    if value == mostnum:
        print(key)