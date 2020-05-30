"""
위장
"""


def solution(clothes):
    clothes_dict = {}
    for c, c_class in clothes:
        if c_class in clothes_dict:
            clothes_dict[c_class] += 1
        else:
            clothes_dict[c_class] = 1
    answer = 1
    for key in clothes_dict:
        answer *= clothes_dict[key]+1
    return answer-1

