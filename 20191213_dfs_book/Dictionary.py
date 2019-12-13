#-*- coding:utf-8 -*-

"""
DICTIONARY 고대어 사전

입력으로 들어온 고대어 단어들을 기준으로 고대어의 알파벳 순서를 유추하는 문제
알파벳 순서의 모순이 있다면 INVALID HYPOTHESIS

ex)
gg
kia
lotte
lg
hanhwa

알고리즘: DFS, 위상정렬

1. dfs를 실행, 첫번째 문자들을 검사한다.
2. 다음 것과 같지 않으면 path에 추가
3. 같으면 첫번째 문자를 제외한 두 단어를 stack에 추가
"""