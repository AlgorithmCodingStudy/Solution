import copy


def check_prime_number(m):
    if m <= 1:
        return False
    if m == 2 or m == 3:
        return True
    if m % 2 == 0:
        return False
    for i in range(3, int(m**0.5)+2, 2):
        if m % i == 0:
            return False
    return True


def permutations(numbers, l, topick):
    if topick == 0:
        return [l]
    answer_tmp = []
    for i, num in enumerate(numbers):
        l.append(num)
        tmp = list(copy.deepcopy(numbers))
        tmp[i] = ""
        tmp = "".join(tmp)
        answer_tmp.append(copy.deepcopy(permutations(tmp, l, topick-1)))
        l.pop()
    answer = sum(answer_tmp, [])
    return answer


def get_set(numbers):
    data = []
    for i, n in enumerate(numbers):
        l = []
        tmp = permutations(numbers, l, i+1)
        data.append(tmp)
    case = []
    for d in data:
        for k in d:
            case.append("".join(k))
    case = set(map(int, case))
    return case


def solution(numbers):
    case = get_set(numbers)

    answer = 0
    for c in case:
        answer += check_prime_number(c)

    return answer


if __name__ == '__main__':
    # print(solution("17"))
    print(solution("0011"))