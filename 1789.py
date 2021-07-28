s = int(input())
num = 0
i = 1
while num <= s:
    num += i
    i += 1
print(i-2) # i의 이전값을 더하고 i를 증가 시키기 떄문에 -2를 합니다
