def check_prime_number_up_to(n):
    seive = [False, False] + [True] * (n-1)
    for i, e in enumerate(seive):
        if e:
            k = i * 2
            while k <= n:
                seive[k] = False
                k += i
    return seive


if __name__ == '__main__':
    case = []
    n = 1
    while n:
        n = int(input())
        case.append(n)
    case.pop()

    for n in case:
        primes = check_prime_number_up_to(2*n)[n+1:]
        print(sum(primes))
