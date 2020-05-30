"""
위장
"""

from functools import reduce
from operator import mul


def solution(clothes):
    clothes_dict = {"_": 1}
    for c, c_class in clothes:
        if c_class in clothes_dict:
            clothes_dict[c_class] += 1
        else:
            clothes_dict[c_class] = 2
    return reduce(mul, clothes_dict.values())-1
