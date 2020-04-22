"""
2477 차량 정비소

손님들은 tk 시간에 맞춰 들어오고
접수 창구에서 ai 만큼 시간을 소비하고
정비 창구에서 bi 만큼 시간을 소비한다.

접수 창구에서는
    1. 고객번호가 낮은 순
    2. 빈 창구가 여러 곳이면 번호가 작은 곳으로

정비 창구에서는
    1. 먼저 기다리는 고객 순
        1. 동시에 접수 창구에서 끝났으면 이용했던 접수 창구번호가 작은 고객이 우선
    2. 빈 창구가 여러 곳이면 번호가 작은 곳으로

지갑을 잃어버린 손님이 이용한 창구들을 사용한 손님의 번호의 합을 출력
"""

T = int(input())
for test_case in range(1, 1 + T):
    N, M, K, A, B = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    t = list(map(int, input().split()))

    A, B = A - 1, B - 1
    waiting1 = []  # A 대기열
    AA = [None] * N  # A 창구
    AA_num = 0  # A 창구 인원
    waiting2 = []  # B 대기열
    BB = [None] * M  # B 창구
    sub_res = [False] * (K + 1)  # 지갑 떨어뜨린 A 창구에 방문한 손님
    result = 0

    time = 0
    idx = 1  # 손님 번호
    while t or AA_num or waiting2:

        # 입장 손님 A 대기열로
        while t and t[0] == time:
            t.pop(0)
            waiting1.append(idx)
            idx += 1

        # A 대기열 -> A창구 -> B 대기열
        for i in range(N):
            # 창구에 손님 있으면
            if AA[i]:
                AA[i][1] -= 1  # 시간 줄임
                if not AA[i][1]:  # 시간 다 되면
                    waiting2.append(AA[i][0])  # B 대기열로 보내고
                    AA[i] = None  # 창구 비움
                    AA_num -= 1

            # 창구 비면
            if AA[i] is None:
                if waiting1:  # A 대기열있으면 채움
                    num = waiting1.pop(0)
                    AA[i] = [num, a[i]]
                    AA_num += 1
                    if i == A:  # 지갑 떨어뜨린 A 창구이면
                        sub_res[num] = True

        # B 대기열 -> B 창구 -> 귀가
        for i in range(M):
            # 창구에 손님 있으면
            if BB[i]:
                BB[i][1] -= 1  # 시간 줄임
                if not BB[i][1]:  # 시간 다 되면 창구 비움
                    BB[i] = None

            # 창구 비면
            if BB[i] is None:
                if waiting2:  # B 대기열있으면 채움
                    num = waiting2.pop(0)
                    BB[i] = [num, b[i]]
                    # 지갑 떨어뜨린 B 창구이면서 A 창구이면 결과 반영
                    if i == B and sub_res[num]:
                        result += num
        # 시간 지남
        time += 1

    # 손님 없으면
    if not result:
        result = -1

    print('#{} {}'.format(test_case, result))
