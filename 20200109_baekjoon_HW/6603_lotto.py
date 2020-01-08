"""
6603 로또

1-49에서 6개를 고른다.
먼저 k개를 고르고 k개의 숫자에서 조합을 만든다.

알고리즘: 조합

1. itertools의 combination 사용
2. 직접 짜기
"""

import sys
read = sys.stdin.readline
from itertools import combinations


def get_combinations_use_itertools(k, s):
    result = combinations(s, 6)
    for r in result:
        print(" ".join(map(str, r)))
    print()


def get_combinations(k, s):
    def combination(arr, r):
        # 1.
        arr = sorted(arr)

        # 2.
        def generate(chosen):
            if len(chosen) == r:
                print(" ".join(map(str, chosen)))
                return

            start = arr.index(chosen[-1]) + 1 if chosen else 0
            for nxt in range(start, len(arr)):
                chosen.append(arr[nxt])
                generate(chosen)
                chosen.pop()
        generate([])

    combination(s, 6)
    print()


while True:
    data = list(map(int, read().strip().split()))
    if data == [0]:
        break
    k, s = data[0], data[1:]
    get_combinations(k, s)
