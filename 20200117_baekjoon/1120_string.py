"""
1120 문자열

길이가 같은 문자열 X와 Y의 차이는 X[i] != Y[i]인 개수이다.

A와 B가 주어지는데 A는 B보다 길이가 같거나 작을 수 있다.
만약 작다면 두가지 연산을 할 수 있다.
    1. 앞에 아무거나 더하기
    2. 뒤에 아무거나 더하기

A와 B의 차이가 최소가 될 때 차이를 출력하라.

알고리즘: 시뮬레이션

1. A와 B의 correlation을 구한다.
2. A의 길이 - correlation의 max를 출력
"""

from sys import stdin
read = stdin.readline

a, b = read().strip().split()


def calculate_correlation(t1, t2):
    def get_same(arr1, arr2):
        result = 0
        for v1, v2 in zip(arr1, arr2):
            if v1 == v2:
                result += 1
        return result

    correlation = []
    for i in range(len(t2) - len(t1) + 1):
        correlation.append(get_same(t1, t2[i:i+len(t1)]))

    return correlation


corr = calculate_correlation(a, b)
print(len(a) - max(corr))
