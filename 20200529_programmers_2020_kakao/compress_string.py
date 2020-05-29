def solution(s):
    def compress(string, unit):
        res = ''
        before, count = string[:unit], 1
        string_divide = [string[i:i + unit] for i in range(0, len(string), unit)]
        for c in string_divide[1:]:
            if before == c:
                count += 1
            else:
                if count == 1:
                    res = "{}{}".format(res, before)
                else:
                    res = "{}{}{}".format(res, count, before)
                before = c
                count = 1
        if count == 1:
            res = "{}{}".format(res, before)
        else:
            res = "{}{}{}".format(res, count, before)
        return len(res)

    min_len = len(s)
    max_divide = len(s) // 2 + 1
    for i in range(1, max_divide):
        min_len = min(compress(s, i), min_len)
    return min_len
