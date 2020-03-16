# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
n = int(input())

if n == 2:
    print(1)
elif n == 3:
    print(7)
else:
    num = '1' * (n//2)
    if n % 2 == 0:
        print(num)
    else:
        num = list(num)
        num[-1] = '7'
        print("".join(num))
