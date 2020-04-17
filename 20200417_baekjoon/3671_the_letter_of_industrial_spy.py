"""
3671 산업스파이의 편지

주어진 숫자를 사용해서 만들수 있는 소수의 갯수를 구해라.

알고리즘: 조합

1. 주어진 숫자의 길이만큼 반복
    1. 1개 뽑아서 만들 수 있는 수 2개 뽑아서...
        1. 하나씩 가져오면서 소수인지 체크

소수를 9999999까지 미리 다 구해두자.
"""
from itertools import permutations
import sys
read = sys.stdin.readline

n = 10000000
a = [False,False] + [True]*(n-1)
primes = []

for i in range(2, n+1):
    if a[i]:
        primes.append(i)
        for j in range(2*i, n+1, i):
            a[j] = False


def get_the_number_of_prime_number(ns):
    def get_pn(un):
        cnt = 0
        cases = set(map(lambda x: "".join(map(str, x)), permutations(ns, un)))
        for case in cases:
            if case[0] == '0':
                continue
            num = int(case)
            if a[num]:
                cnt += 1
        return cnt

    pn_cnt = 0
    for use_num in range(1, len(ns)+1):
        pn_cnt += get_pn(use_num)
    return pn_cnt


for _ in range(int(read())):
    nums = list(map(int, list(read().strip())))
    print(get_the_number_of_prime_number(nums))
