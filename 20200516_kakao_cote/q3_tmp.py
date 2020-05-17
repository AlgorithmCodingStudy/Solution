#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'scatterPalindrome' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY strToEvaluate as parameter.
#
def scatterPalindrome(strToEvaluate):
    def check_palindrome(s):
        dict_s = {}
        for c in s:
            if c in dict_s:
                dict_s[c] += 1
            else:
                dict_s[c] = 1

        once = False
        for k in dict_s.keys():
            if dict_s[k] % 2:
                if not once:
                    once = True
                else:
                    return False
        return True

    # Write your code here
    result = []
    for now_str in strToEvaluate:
        cnt = 0
        now_str = list(now_str)
        for i in range(len(now_str)):
            dict_c = {}
            for j in range(i, len(now_str)):
                # if i == j: continue
                if now_str[j] in dict_c:
                    dict_c[now_str[j]] += 1
                else:
                    dict_c[now_str[j]] = 1

                once = False
                fail = False
                for k in dict_c.keys():
                    if dict_c[k] % 2:
                        if not once:
                            once = True
                        else:
                            fail = True
                            break
                if fail:
                    continue
                else:
                    cnt += 1

        result.append(cnt)
    return result


if __name__ == '__main__':
    print(scatterPalindrome(["bbrrg"]))
