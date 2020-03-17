"""
땅따먹기

열의 개수가 4인 곳을 한칸씩 밟으며 내려오는데
밟은 열은 다음 행에서 같은 열을 밟을 수 없다.
얻을 수 있는 최대 값은?

알고리즘 : DP

4가지 경우의 수가 생긴다.
4가지 경우에 대해 최대를 다 구해가서 마지막에 최대를 비교하자.
"""
def solution(land):
    line = land[0]
    answer = [[0, line[0]], [1, line[1]], [2, line[2]], [3, line[3]]]
    for line in land[1:]:
        nxt_answer = []
        for j, (pos, value) in enumerate(answer):
            tmp = line[pos]
            line[pos] = 0
            max_value = max(line)
            line[pos] = tmp
            for i, v in enumerate(line):
                if i == pos: continue
                else:
                    if v == max_value:
                        nxt_answer.append([i, value+v])
        answer = nxt_answer
    answer = max([b for a, b in answer])
    return answer


print(solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]]))