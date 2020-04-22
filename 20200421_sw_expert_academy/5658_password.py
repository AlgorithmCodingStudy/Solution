"""
5658 보물상자 비밀번호

n은 주어지는 숫자의 수
k는 k번째로 큰 수
주어진 n개의 16진수가 n/4로 그룹을 가진다.
회전하면 한칸씩 밀리는데 가능한 모든 수에서 k번째로 큰 수를 골라라.
"""
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    nums = list(input())
    length_of_password = n//4
    cases = set()
    for _ in range(length_of_password):
        for i in range(0, n, length_of_password):
            case = nums[i:i+length_of_password]
            cases.add(tuple(case))

        nums = [nums[-1]] + nums[:-1]
    cases = sorted(cases, reverse=True)
    result = int("".join(cases[k-1]), 16)
    print("#{} {}".format(test_case, result))
