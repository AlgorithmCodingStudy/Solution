"""
2117 홈 방범 시스템

지역 크기 N 5 <= N <= 20
하나의 집이 지불하는 비용 M 1 <= M <= 10
서비스 영역 크기 K

운영 비용 : K*K + (K-1)*(k-1)

이익 = 집 * M - 운영비용

손해가 나지 않으면서 가장 많은 집을 서비스할 수 있는 경우의 집 수를 출력

집 1 지역 0
"""

import sys
sys.stdin = open("input.txt", "r")


def count_home(x, y):
    def check_range(x_, y_):  # 범위 체크
        return 0 <= x_ < n and 0 <= y_ < n

    cnt = 0
    for dx in range(-(k-1), k):  # k가 4면 dx는 -3 ~ 3
        if dx <= 0:  # 운영지역의 윗부분
            for dy in range(-(k+dx-1), k+dx):  # k가 4, dx가 -3이면 dy는 0 ~ 0, dx가 -2면 dy는 -1 ~ 1
                nx, ny = x+dx, y+dy
                if not check_range(nx, ny): continue
                if area[nx][ny] == 1:  # 집이면 cnt += 1
                    cnt += 1

        else:  # 운영지역의 아랫부분
            for dy in range(-(k-dx-1), k-dx):
                nx, ny = x+dx, y+dy
                if not check_range(nx, ny): continue
                if area[nx][ny] == 1:
                    cnt += 1

    benefit = cnt * m - (k**2 + (k-1)**2)  # 이익 계산
    if benefit >= 0:  # 손해가 나지 않으면
        return cnt
    else:
        return 0


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////

    n, m = map(int,  input().split())
    area = [list(map(int, input().split())) for _ in range(n)]

    max_home = 0
    for k in range(1, n+2):  # 운영지역을 넓혀가며 테스트, n+2까지 검토해야 모든 경우의 수
        for i in range(n):  # 운영지역의 중간지점을 한칸씩 옮겨가며 전체 검토
            for j in range(n):
                home = count_home(i, j)  # k와 중간지점이 결정된 상태에서 수익을 검토하고 손해가 나지 않았으면 집의 수를 리턴
                if home > max_home:  # 최대값과 비교
                    max_home = home

    print("#{} {}".format(test_case, max_home))
    # ///////////////////////////////////////////////////////////////////////////////////
