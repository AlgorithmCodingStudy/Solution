if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    a.insert(0, 0)

    max = 0
    d = [1 for _ in range(n)]
    d.insert(0, 0)
    for i in range(1, n+1):
        for j in range(1, i):
            if a[j] < a[i] and d[i] < d[j] + 1:
                d[i] = d[j] + 1

        if max < d[i]:
            max = d[i]

    print(max)