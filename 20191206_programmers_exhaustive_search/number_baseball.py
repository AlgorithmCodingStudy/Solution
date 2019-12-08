from itertools import permutations


def check_score(case, question, s, b):
    strike = 0
    for i in range(3):
        if case[i] == question[i]:
            strike += 1
    if s != strike:
        return False

    ball = 0
    for i in range(3):
        for j in range(3):
            if case[i] == question[j] and i != j:
                ball += 1
    if b != ball:
        return False

    return True


def solution(baseball):
    answer = 0
    all_case = list(permutations(range(1, 10), 3))

    for case in all_case:
        for question, s, b in baseball:
            question = (question//100, question%100//10, question%10)
            if check_score(case, question, s, b):
                test = True
            else:
                test = False
                break
        if test:
            answer += 1

    return answer

if __name__ == '__main__':
    print(solution([[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]]))