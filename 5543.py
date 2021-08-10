high = int(input())
middle = int(input())
low = int(input())
coke = int(input())
soda = int(input())
cheep = 4000
buger = [high, middle, low]
drink = [coke, soda]
for i in range(0, len(buger)):
    for k in range(0, len(drink)):
        if buger[i] + drink[k] < cheep:
            cheep = buger[i] + drink[k]
print(cheep-50)