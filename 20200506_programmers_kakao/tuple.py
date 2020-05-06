"""
튜플

주어진 문자열을 튜플로 만들어라.

알고리즘: 문자열

1. 앞뒤에 중괄호 제거
2. ,를 기준으로 split
    1. 하나씩 가져오며 앞뒤 중괄호 제거
    2. ,를 기준으로 split하며 map으로 int로 바꾸기
    3. set에 담기
3. 모든 set union
"""


def solution(s):
    s = s[2:-2]
    s = s.split('},{')
    s = list(sorted(map(lambda x: list(map(int, x.split(','))), s), key=len))
    answer = []
    for v in s:
        add = set(v) - set(answer)
        answer.extend(list(add))
    return list(answer)


print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
