if __name__ == '__main__':
    s = list(map(int, input().split()))
    n = list(map(int, input().split()))
    u = list(map(int, input().split()))

    result = []
    for price, weight in [s, n, u]:
        weight_sum = weight * 10
        price_sum = price * 10 * 1
        if price_sum >= 5000:
            price_sum -= 500
        price_per_weight = weight_sum / price_sum
        result.append(price_per_weight)

    result_max = zip(result, range(0, len(result)))
    idx = max(result_max)[1]
    if idx == 0:
        print("S")
    elif idx == 1:
        print("N")
    else:
        print("U")