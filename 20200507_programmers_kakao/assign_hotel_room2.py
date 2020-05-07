"""
호텔 방 배정

호텔 방을 배정한다.
    1. 신청한 순서대로 한명씩
    2. 원하는 방이 비어있으면 바로 배정
    3. 없다면 원하는 방보다 크면서 가장 작은 방 배정
배정된 방 번호를 출력

알고리즘: 시뮬레이션
"""
import sys
sys.setrecursionlimit(10000000)


def find_empty_room(x, rooms):
    if x not in rooms:
        rooms[x] = x + 1
        return x

    p = find_empty_room(rooms[x], rooms)
    rooms[x] = p + 1
    return p


def solution(k, room_number):
    room_state = {}
    answer = []
    for n in room_number:
        answer.append(find_empty_room(n, room_state))

    return answer


print(solution(10, [1,3,4,1,3,1]))
