count = 1
div_list = []
for _ in range(0, 10):
    num = int(input())
    div_list.append(num%42)
print(len(set(div_list)))