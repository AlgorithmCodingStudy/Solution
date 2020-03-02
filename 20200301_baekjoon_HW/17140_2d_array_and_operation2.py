r, c, k = map(int, input().split())
arr = [list(map(int, input().split())) + [0] * 97 if _ < 3 else [0] * 100 for _ in range(100)]


def single_sort(lst):
    cnt_nums = {}
    for i in lst:
        if i == 0:
            continue
        if i in cnt_nums:
            cnt_nums[i] += 1
        else:
            cnt_nums[i] = 1
    sorted_nums = [[key, val] for key, val in cnt_nums.items()]
    sorted_nums.sort(key=lambda x: (x[1], x[0]))

    temp = [0] * 100
    length = min(len(sorted_nums) * 2, 100)
    max_ = length
    for i in range(length // 2):
        temp[2 * i] = sorted_nums[i][0]
        temp[2 * i + 1] = sorted_nums[i][1]
    return temp, max_


def sort_row(arr):
    global max_cols

    cols = 0
    for y in range(100):
        if sum(arr[y]) == 0:
            break
        else:
            arr[y], max_ = single_sort(arr[y])
            if max_ > cols:
                cols = max_

    max_cols = cols
    return arr


def sort_col(arr):
    global max_rows

    for y in range(100):
        for x in range(100):
            if x > y:
                arr[y][x], arr[x][y] = arr[x][y], arr[y][x]

    rows = 0
    for y in range(100):
        if sum(arr[y]) == 0:
            break
        else:
            arr[y], max_ = single_sort(arr[y])
            if max_ > rows:
                rows = max_
    max_rows = rows

    for y in range(100):
        for x in range(100):
            if x > y:
                arr[y][x], arr[x][y] = arr[x][y], arr[y][x]

    return arr


max_rows, max_cols = 3, 3
cnt = 0

while 1:
    if arr[r - 1][c - 1] == k or cnt > 100:
        break
    cnt += 1
    if max_rows >= max_cols:
        arr = sort_row(arr)
    else:
        arr = sort_col(arr)

if cnt > 100:
    cnt = -1
print(cnt)