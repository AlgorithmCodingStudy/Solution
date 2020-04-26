"""
16919 봄버맨 2

1. 봄버맨이 일부 칸에 폭탄설치
2. 1초 쉬고
3. 1초동안 폭탄이 설치되어 있지 않은 모든 칸에 폭탄 설치
4. 1초가 지난 후 3초전에 설치된 폭탄 모두 폭발

알고리즘: 시뮬레이션


"""

import sys
read = sys.stdin.readline

r, c, n = map(int, read().split())