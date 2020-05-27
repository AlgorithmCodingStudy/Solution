"""
q1 완주하지 못한 선수

마라톤에 참여한 선수들의 이름과 완주한 사람들의 이름이 주어진다.
완주하지 못한 선수의 이름을 return

알고리즘: 해시

1. 두 list를 set으로 변환
2. 차집합
3. 다시 list로 바꾸고 리턴
"""


def solution(participant, completion):
    cs = {}
    for c in completion:
        if c in cs:
            cs[c] += 1
        else:
            cs[c] = 1
    for p in participant:
        if p in cs:
            if cs[p] == 1:
                cs.pop(p)
            else:
                cs[p] -= 1
        else:
            return p


print(solution(['leo', 'kiki', 'eden'], ['eden', 'kiki']))
