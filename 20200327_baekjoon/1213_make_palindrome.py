"""
1213 팰린드롬

입력으로 들어온 알파벳을 재배치해서 팰린드롬으로 만든다.
알파벳순으로 가장 먼저인 것으로 만든다.

알고리즘: 문자열?

1. 문자열을 dictionary로 count를 구한다.
2. 문자열의 길이가 짝수일때
    1. count가 홀수인 것이 존재하면 -1
    2. 키를 sort한다.
    3. 결과에 카운트의 절반씩 추가한다.
    4. 절반을 반대로 복제한다.
3. 문자열의 길이가 홀수일때
    1. count가 홀수인 것이 2개이상이면 -1
    2. count가 홀수인 것에서 하나를 따로 빼놓는다.
    3. 키를 sort한다.
    4. 결과에 카운트의 절반씩 추가한다.
    5. result + center + result_inverse
"""

import sys
read = sys.stdin.readline

name = list(read().strip())
cnt = {}
for ch in name:
    if ch not in cnt:
        cnt[ch] = 1
    else:
        cnt[ch] += 1

result, center = [], ''
for key in sorted(cnt.keys()):
    if cnt[key] % 2:
        if len(name) % 2:
            if not center:
                center = key
                cnt[key] -= 1
            else:
                print("I'm Sorry Hansoo")
                sys.exit(0)
        else:
            print("I'm Sorry Hansoo")
            sys.exit(0)
    result.extend([key]*(cnt[key]//2))

result = result + [center] + result[::-1]
print("".join(result))
