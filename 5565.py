total = int(input())
book = []
temp = 0
for _ in range(0, 9):
    price = int(input())
    book.append(price)
for i in range(0, 9):
    temp += book[i]
last = total - temp
print(last)