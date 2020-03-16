t = int(input())


def check_tile(x, y):
    for dx in range(2):
        for dy in range(2):
            if area[x+dx][y+dy] == 0:
                return False
    return True

def print_tile(x, y):
    for dx in range(2):
        for dy in range(2):
            result[x+dx][y+dy] = 1


for _ in range(t):
    n, m = map(int, input().split())
    area = [list(map(int, input().split())) for _ in range(n)]
    result = [[0]*m for _ in range(n)]
    for i in range(n-1):
        for j in range(m-1):
            if check_tile(i, j):
                print_tile(i, j)

    if area == result:
        print("YES")
    else:
        print("NO")
