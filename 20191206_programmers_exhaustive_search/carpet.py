def check_carpet(brown, red, w, h):
    if w*2 + h*2 - 4 == brown:
        if (w-2)*(h-2) == red:
            return True
    return False


def solution(brown, red):
    answer = []
    n_carpet = brown + red
    for i in range(1, int(n_carpet**0.5)+1):
        if n_carpet % i == 0:
            if check_carpet(brown, red, n_carpet // i, i):
                answer.append(n_carpet//i)
                answer.append(i)
    return answer


if __name__ == '__main__':
    print(solution(10, 2))
    print(solution(8, 1))
    print(solution(24, 24))
    print('test')