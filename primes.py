from collections import defaultdict
from itertools import product
from functools import reduce
from operator import mul


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


def prime_factors(n, prime_list=None):
    if n < 2:
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

    return factor_dict


def is_prime(n, prime_list=None, prime_set=None):
    if n < 2:
        return False
    if prime_set is not None and n in prime_set:
        return True
    if prime_list is None:
        prime_list = primes()
    for p in prime_list:
        if p * p > n:
            break
        if n % p == 0:
            return False
    return True


def gcd(a, b):
    # implements Euclid's algorithm
    if b > a:
        a, b = b, a
    q = int(a // b)
    r = a - q * b
    while r != 0:
        a, b = b, r
        q = int(a // b)
        r = a - q * b
    return int(b)


def is_coprime(j, k):
    return gcd(j, k) == 1


def chinese_remainder(D, Y):
    # Returns the value x (mod M) such that when x is divided by any di in
    # the list of coprime integers D the remainder is the corresponding yi in
    # the list of remainders Y. M is the product of the Ds.

    M = reduce(lambda x, y: x * y, D, 1)
    B = [int(M / d) for d in D]
    A = []
    for d, b in zip(D, B):
        for a in range(1, d):
            if a * b % d == 1:
                A.append(a)
                break

    x = sum([a * b * y for a, b, y in zip(A, B, Y)])
    return x % M
