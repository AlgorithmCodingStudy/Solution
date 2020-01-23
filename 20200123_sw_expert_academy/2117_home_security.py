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

# import sys


'''
      아래의 구문은 input.txt 를 read only 형식으로 연 후,
      앞으로 표준 입력(키보드) 대신 input.txt 파일로부터 읽어오겠다는 의미의 코드입니다.
      여러분이 작성한 코드를 테스트 할 때, 편의를 위해서 input.txt에 입력을 저장한 후,
      아래 구문을 이용하면 이후 입력을 수행할 때 표준 입력 대신 파일로부터 입력을 받아올 수 있습니다.

      따라서 테스트를 수행할 때에는 아래 주석을 지우고 이 구문을 사용하셔도 좋습니다.
      아래 구문을 사용하기 위해서는 import sys가 필요합니다.

      단, 채점을 위해 코드를 제출하실 때에는 반드시 아래 구문을 지우거나 주석 처리 하셔야 합니다.
'''
# sys.stdin = open("input.txt", "r")


def count_home(x, y):
    def check_range(x_, y_):
        return 0 <= x_ < n and 0 <= y_ < n

    cnt = 0
    for dx in range(-(k-1), k):
        if dx <= 0:
            for dy in range(-(k+dx-1), k+dx):
                nx, ny = x+dx, y+dy
                if not check_range(nx, ny): continue
                if area[nx][ny] == 1:
                    cnt += 1
        else:
            for dy in range(-(k-dx-1), k-dx):
                nx, ny = x+dx, y+dy
                if not check_range(nx, ny): continue
                if area[nx][ny] == 1:
                    cnt += 1

    benefit = cnt * m - (k**2 + (k-1)**2)
    if benefit >= 0:
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
    for k in range(1, n+2):
        for i in range(n):
            for j in range(n):
                home = count_home(i, j)
                if home > max_home:
                    max_home = home

    print("#{} {}".format(test_case, max_home))
    # ///////////////////////////////////////////////////////////////////////////////////

