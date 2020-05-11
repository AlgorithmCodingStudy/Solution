#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):
    leaderboard = list(sorted(set(scores), reverse=True))

    res = []
    for alice_score in alice:
        start = 0
        end = len(leaderboard) - 1
        found = False

        while start <= end:
            mid = (start + end) // 2
            if leaderboard[mid] == alice_score:
                idx = mid
                found = True
                res.append(mid + 1)
                break
            elif leaderboard[mid] > alice_score:
                start = mid + 1
            else:
                end = mid - 1
        if not found:
            idx = start
            res.append(idx + 1)
            leaderboard.insert(idx, alice_score)

    return res


if __name__ == '__main__':
    print(climbingLeaderboard([100,100,50,40,40,20,10], [5,25,50,120]))
    print(climbingLeaderboard([100, 90, 90, 80, 75, 60], [50, 65, 77, 90, 102]))