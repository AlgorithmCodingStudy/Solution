from copy import deepcopy
count = 0


def sum_recursion(numbers, result, target):
    global count

    if len(numbers) == 0:
        if result == target:
            count += 1
        return
    else:
        node = numbers.pop(0)
        sum_recursion(deepcopy(numbers), result+node, target)
        sum_recursion(deepcopy(numbers), result-node, target)


def solution(numbers, target):
    sum_recursion(numbers, 0, target)
    answer = count
    return answer


if __name__ == '__main__':
    print(solution([1, 1, 1, 1, 1], 3))