# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
m = int(input())
quantity_tmp = [int(input()) for _ in range(m)]
m = int(input())
price_tmp = [float(input()) for _ in range(m)]

price, quantity = [], []
for q, p in zip(quantity_tmp, price_tmp):
    if p > 0:
        quantity.append(q)
        price.append(p)

m = len(price)

quantity_tmp2 = quantity + [n]
quantity_tmp2.sort()
pos = quantity_tmp2.index(n)

if pos == 0:
    left, right = 0, 1
    if m == 1:
        print(price[0])
        exit()
elif pos == m:
    left, right = m-2, m-1
else:
    left, right = pos-1, pos

delta = (price[right] - price[left]) / (quantity[right] - quantity[left])
result = price[left] + delta * (n - quantity[left])

round_2 = round(result, 2)
round_3 = round(result, 3)
if round(round_3 - round_2, 3) == 0.005:
    round_2 += 0.01

print(round_2)