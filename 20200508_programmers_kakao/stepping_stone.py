"""
징검다리 건너기

stones라는 배열에 밟을 수 있는 횟수가 있다.
밟을 수 있다면 밟고 아니면 건너뛴다.
그대신 k개 까지 건널 수 있으며 그 이상 거리가 멀면 종료된다.
몇명 건널 수 있을까?

알고리즘: union-find..?

1. 하나씩 다 검토하는데
    1. 0이면 카운트+1
        1. 카운트 > k 면 종료
    2. 0이 아니면 -1
2. 종료후 검토한 횟수 출력

근데 아마 느리겠지..
"""


def solution(stones, k):
    answer, finish = -1, False
    while not finish:
        cnt = 0
        for i, st in enumerate(stones):
            if st == 0:
                cnt += 1
                if cnt > k-1:
                    finish = True
                    break
            else:
                cnt = 0
                stones[i] -= 1
        answer += 1
    return answer

print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))