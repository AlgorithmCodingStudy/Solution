"""
q2 전화번호 목록

번호가 주어지는데 어느 한 번호가 다른 번호의 접두어인 경우면 false 아니면 true

알고리즘: 해시

1. 1,000,000 * 1,000,000 = 1,000,000,000,000 시간초과 각
"""


def solution(phone_book):
    phone_book.sort()
    for i, p1 in enumerate(phone_book):
        for j, p2 in enumerate(phone_book):
            if i == j: continue
            if len(p1) > len(p2): continue
            if p1 in p2[:len(p1)]:
                return False
    return True
