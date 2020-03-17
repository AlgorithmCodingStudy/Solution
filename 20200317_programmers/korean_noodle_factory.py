"""
라면 공장

밀가루를 공급 받아 공장을 운영해야한다.
stock 남아있는 밀가루 4
dates 밀가루 공급 일정 [4, 10, 15]
supplies 밀가루 공급량 [20, 5, 10]
k 버텨야하는 날짜 30

알고리즘 : 시뮬레이션

현재 남아있는 밀가루를 기준으로 향후 며칠안에 밀가루 공급일정이 있는지 본다.
1. 만약 일정이 한개라면
    1. 그거 받기
2. 일정이 두개 이상이라면
    1. 받는 날짜의 stock + 밀가루 공급량 supplies을 비교해서 가장 큰 경우로

날짜를 하루하루 진행하며
1. 밀가루 공급날에 도착하면
    1. 받을지 말지 고민
        1. 그걸로 k를 넘으면 무조건 받기
        2. 내가 현 위치 stock + 받는 supplies vs 다음 공급 위치 stock + 받는 supplies 비교

heap...
날짜를 진행하다가 공급날짜를 만나면 공급을 받고 안받고 삽입 근데 stock을 기준으로 priority queue?
"""
import heapq

def solution(stock, dates, supplies, k):
    answer = 0
    h = []
    d = 0
    while stock < k:
        while d < len(dates) and dates[d] <= stock:
            heapq.heappush(h, -supplies[d])
            d += 1
        stock += -heapq.heappop(h)
        answer += 1
    return answer


print(solution(4, [4, 10, 15], [20, 5, 10], 30))