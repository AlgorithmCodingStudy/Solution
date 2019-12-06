def solution(answers):
    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    result = [0, 0, 0]
    for i, correct in enumerate(answers):
        if a[i % 5] == correct:
            result[0] += 1
        if b[i % 8] == correct:
            result[1] += 1
        if c[i % 10] == correct:
            result[2] += 1

    max_count = max(result)
    answer = []
    if result[0] == max_count:
        answer.append(1)
    if result[1] == max_count:
        answer.append(2)
    if result[2] == max_count:
        answer.append(3)

    return answer


if __name__ == '__main__':
    print(solution([1, 2, 3, 4, 5]))
    print(solution([1, 3, 2, 4, 2]))
    print(solution([2, 1, 2, 3, 2, 4, 2, 5]))
    print(solution([2, 2, 3, 3, 3]))