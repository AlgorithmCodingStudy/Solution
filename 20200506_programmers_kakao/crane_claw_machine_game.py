"""
크레인 인형뽑기 게임

board와 moves가 주어지면 그대로 실행한후 터진 인형의 개수를 구하라.
같은 인형이 만난다면 터진다.

알고리즘: 시뮬레이션

1. get(col) 함수를 만들어서 그 column에 인형을 가져온다.
2. put() 함수를 만들어서 stack에 넣으면서 같은 인형이 나오면 터트린다.
3. 터진 인형 수 출력
"""


def solution(board, moves):
    n = len(board)
    stack = []
    answer = 0

    def get(j):
        for i in range(n):
            if board[i][j] == 0:
                continue
            else:
                result = put(board[i][j])
                board[i][j] = 0
                return result
        return 0

    def put(v):
        if stack and stack[-1] == v:
            stack.pop()
            return 2
        else:
            stack.append(v)
            return 0

    for move in moves:
        answer += get(move-1)

    return answer


print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))
