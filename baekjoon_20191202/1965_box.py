if __name__ == '__main__':
    n = int(input())
    boxes = list(map(int, input().split()))
    boxes.insert(0, 0)

    a = list(zip(boxes, range(len(boxes))))

    d = [0]
    for box, i in a:
        if i == 0:
            continue

        a_before = a[:i]

        a_small = list(map(lambda x: x if x[0] < box else None, a_before))
        while None in a_small:
            a_small.remove(None)

        a_small_idx = list(map(lambda x: x[1], a_small))

        d_max = 0
        for k in a_small_idx:
            if d[k] > d_max:
                d_max = d[k]

        d.append(d_max+1)

    print(max(d))