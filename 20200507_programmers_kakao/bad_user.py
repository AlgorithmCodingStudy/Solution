"""
불량 사용자

응모자 아이디가 주어지고 불량사용자 아이디가 주어진다.
불량사용자 아이디는 *로 몇개 가려진 상태고
제재 아이디는 불량사용자 아이디로부터 추정된 아이디들이다.
가능한 경우의 수를 구하라.

알고리즘: 문자열, 조합

1. 불량사용자를 하나씩 가져오며 응모자 아이디로부터 가능한 아이디들을 모두 저장한다.
2. 제재 아이디를 하나씩 고르는데
    1. 이미 고른 아이디에 내가 고를 아이디가 있으면 안되고
    2. 다 골랐는데 이미 경우의 수 안에 있다면 담지 않기
3. 경우의 수 출력
"""


def solution(user_id, banned_id):
    available_list = []
    for i, ban_id in enumerate(banned_id):
        star_indice = []
        while True:
            tmp = ban_id.find("*")
            if tmp == -1:
                break
            else:
                star_indice.append(tmp)
                ban_id = ban_id[:tmp]+ban_id[tmp+1:]
        available = []
        for j, u_id in enumerate(user_id):
            if len(banned_id[i]) != len(user_id[j]):
                continue

            for idx in star_indice:
                u_id = u_id[:idx]+u_id[idx+1:]
            if u_id == ban_id:
                available.append(user_id[j])
        available_list.append(available)

    result_list = set()

    def combination(chosen):
        if len(chosen) == len(banned_id):
            result_list.add(tuple(sorted(chosen)))
            return

        start = len(chosen)
        for now_id in available_list[start]:
            if now_id not in chosen:
                combination(chosen+[now_id])

    combination([])

    return len(result_list)


print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]))
