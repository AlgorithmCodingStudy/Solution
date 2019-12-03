if __name__ == '__main__':
    n = int(input())
    boxes = list(map(int, input().split()))

    max_count = -1

    for i, data in enumerate(boxes):
        if i == 0: continue
        count = 0
        before = -1
        for tmp in boxes[0:i]:
            if data > tmp and tmp > before:
                count += 1
            before = tmp
        if count > max_count:
            max_count = count


    box = zip(boxes, range(0, len(boxes)))
    idx = max(box)[1]

    pass