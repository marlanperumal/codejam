from collections import defaultdict
from itertools import product, takewhile
from functools import reduce
from operator import mul


def take_less_than(n, iterable):
    return list(takewhile(lambda x: x < n, iterable))


def primes():
    yield 2

    composites = defaultdict(list)
    i = 1
    while True:
        i += 2
        if i in composites:
            composite = composites.pop(i)
            for j in composite:
                composites[i + 2 * j].append(j)
        else:
            composites[3 * i].append(i)
            yield i


def factors(n, prime_list=None):
    if n < 1:
        raise ValueError
    factor_dict = defaultdict(int)
    if prime_list is None:
        prime_list = primes()

    for p in prime_list:
        while n % p == 0:
            n /= p
            factor_dict[p] += 1
        if n == 1:
            break
    factor_list = []

    for powers in product(*[list(range(j + 1)) for j in factor_dict.values()]):
        factor_list.append(reduce(mul, [p**powers[i] for i, p in enumerate(factor_dict)], 1))

    return sorted(factor_list)


def search(j, p, s, N, max_j):
    if s == N:
        return max(j, max_j)
    i = 2
    new_s = s + i * p
    j += 1
    while new_s <= N:
        max_j = search(j, i * p, new_s, N, max_j)
        i += 1
        new_s += p
    return max_j


def run(N):
    max_j = 0
    for i in factors(N, prime_list):
        if i < 3:
            continue
        max_j = search(1, i, i, N, max_j)
    return max_j


prime_list = take_less_than(1e6, primes())

T = int(input())

for t in range(1, T + 1):
    N = int(input())
    result = run(N)
    print(f"Case #{t}: {result}")
