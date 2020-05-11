#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'maximumProfit' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY price as parameter.
#
"""
0
197
3
"""


def maximumProfit(price):
    def to_max(arr, v):
        if len(arr) == 0:
            return v
        max_v = max(arr)
        idx = arr.index(max_v)
        v += max_v * idx - sum(arr[:idx])
        return to_max(arr[idx + 1:], v)

    return to_max(price, 0)


print(maximumProfit([5, 3, 2]))
print(maximumProfit([1, 2, 100]))
print(maximumProfit([1, 3, 1, 2]))

