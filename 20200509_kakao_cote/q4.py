"""
6
2
PPSRP

1

43
32
PSPPSPRSPSPSPPSRSPRSRPPPPRSSSSRPSPRRSSPSPP

2
"""
# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
a = int(input())
formations = list(input())

if len(formations) == a:
    formations.append('o')
elif a % 2 == 0:
    formations.insert(a+1, 'o')
else:
    formations.insert(a, 'o')

cnt = 0


def who_win(l, r):
    if (l == 'R' and r == 'S') or (l == 'S' and r == 'R'):
        return 'R'
    elif (l == 'S' and r == 'P') or (l == 'P' and r == 'S'):
        return 'S'
    elif (l == 'P' and r == 'R') or (l == 'R' and r == 'P'):
        return 'P'

def i_win(enemy):
    if enemy == 'S':
        return 'r'
    elif enemy == 'P':
        return 's'
    elif enemy == 'R':
        return 'p'

def nxt_round(form):
    if len(form) == 1:
        return
    nxt = []
    for i in range(0, len(form)-1, 2):
        left, right = form[i], form[i+1]
        if left.islower() or right.islower():
            if left.islower():
                poi, enemy = left, right
            else:
                poi, enemy = right, left
            win = i_win(enemy)
            if poi != win and poi != 'o':
                global cnt
                cnt += 1
            nxt.append(win)
        else:
            win = who_win(left, right)
            if win != None:
                nxt.append(win)
    if len(form) % 2 == 1:
        nxt.append(form[-1])
    nxt_round(nxt)


nxt_round(formations)
print(cnt)
