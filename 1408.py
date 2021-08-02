nHour, nMin, nSec = map(int, input().split(':'))
fHour, fMin, fSec = map(int, input().split(':'))
now, finish, temp = 0, 0, 0
hour, min, sec = 0, 0, 0
now = nHour * 3600 + nMin * 60 + nSec #1시간 3600초, 1분 60초
finish = fHour *3600 + fMin *60 + fSec
temp = finish - now
if temp < 0:
    temp += 60*60*24 #60초 60분 24시간
hour = temp // 3600
min = (temp%3600) // 60
sec = (temp%3600) % 60
if sec < 10:
    sec = '0'+str(sec)
if min < 10:
    min = '0'+str(min)
if hour < 10:
    hour = '0'+ str(hour)
print(str(hour) + ':' + str(min) + ':' + str(sec))