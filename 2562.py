import sys
num_list = []
for _ in range(0,9):
    num = int(sys.stdin.readline())
    num_list.append(num)
max = 0
position = 0
for i in range(0, len(num_list)):
    if num_list[i] > max:
        max = num_list[i]
        position = i+1
print(max)
print(position)