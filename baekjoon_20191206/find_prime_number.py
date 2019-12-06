import itertools


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


def solution(numbers):
    # numbers_list = list(map(int, numbers))
    data = []
    for i, n in enumerate(numbers):
        data.append(list(itertools.permutations(numbers, i+1)))
    case = []
    for d in data:
        for k in d:
            case.append("".join(k))
    case = set(map(int, case))

    answer = 0
    for c in case:
        answer += check_prime_number(c)

    return answer


if __name__ == '__main__':
    print(solution("17"))
    print(solution("0011"))