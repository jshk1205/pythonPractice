ptotal = 0
pmax = []
for _ in range(0, 10):
    pout, pin = map(int, input().split())
    ptotal += pin
    ptotal -= pout
    pmax.append(ptotal)
print(max(pmax))