"""
호텔 방 배정

호텔 방을 배정한다.
    1. 신청한 순서대로 한명씩
    2. 원하는 방이 비어있으면 바로 배정
    3. 없다면 원하는 방보다 크면서 가장 작은 방 배정
배정된 방 번호를 출력

알고리즘: 시뮬레이션
"""


def solution(k, room_number):
    answer = []
    room_state = [False]*k
    for n in room_number:
        if not room_state[n-1]:
            room_state[n-1] = True
            answer.append(n)
        else:
            for i in range(n, k):
                if not room_state[i]:
                    room_state[i] = True
                    answer.append(i+1)
                    break

    return answer


print(solution(10, [1,3,4,1,3,1]))
