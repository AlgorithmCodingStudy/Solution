"""
16637 괄호 추가하기

길이가 N인 수식을 앞에서부터 차례로 계산한다.
여기에 이제 괄호를 추가해서 식에 변형을 준다.
중첩된 괄호는 사용할 수 없다.

알고리즘: DFS, 브루트 포스

1. 재귀
    1. 계산할 수 있는 경우
        1. (3+8)*7-9*2 = 11*7-9*2
        2. 3+(8*7)-9*2 = 3+56-9*2
        3. 3+8*(7-9)*2 = 3+8*-2*2
        4. 3+8*7-(9*2) = 3+8*7-18
        답이 계산되면 대소비교

"""
from copy import deepcopy
from itertools import combinations
import sys
read = sys.stdin.readline

n = int(read().strip())
e = list(read().strip())
if n == 1:
    print(e[0])
    sys.exit(0)

max_value = -2e31
choice = list(range(n//2))
for i in choice:
    cases = list(combinations(choice, i))
    for case in cases:
        flag = True
        for j, v in enumerate(case[:-1]):
            if case[j+1] - v == 1:
                flag = False
                break
        if not flag: continue
        eval_e = deepcopy(e)
        for j in range(len(case)):
            idx = case[j]-j
            value = eval("".join(eval_e[2*idx:2*idx+3]))
            eval_e = eval_e[:2*idx]+[str(value)]+eval_e[2*idx+3:]
        for j in range(len(eval_e)//2):
            value = eval("".join(eval_e[:3]))
            eval_e = [str(value)]+eval_e[3:]
        max_value = max(max_value, int(eval_e[0]))

print(max_value)
