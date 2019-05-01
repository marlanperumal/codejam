from random import randint


def Rn(i, n):
    return 2**(int(n // i))


num_ring_types = 6

# R = [100 if r == 0 else randint(0, 100) for r in range(num_ring_types)]
R = [100, 100, 100, 100, 100, 100]
print(R)
print([int(56 // (i + 1)) for i in range(num_ring_types)])
print([2**int(56 // (i + 1)) for i in range(num_ring_types)])
R52 = [r * Rn(i + 1, 180) for i, r in enumerate(R)]
R56 = [r * Rn(i + 1, 56) for i, r in enumerate(R)]
print(R52, sum(R52) % 2**63)
print(R56, sum(R56) % 2**63)

R52 = sum(R52)
R56 = sum(R56)

r1 = int(R56 // 2**56)
R56 -= r1 * 2**56
r2 = int(R56 // 2**28)
R56 -= r2 * 2**28
r3 = int(R56 // 2**18)
while r3 >= 0:
    R56_1 = R56 - r3 * 2**18
    r4 = int(R56_1 // 2**14)
    while r4 >= 0 and r4 <= 100:
        R56_2 = R56_1 - r4 * 2**14
        r5 = int(R56_2 // 2**11)
        while r5 >= 0 and r5 <= 100:
            R56_3 = R56_2 - r5 * 2**11
            r6 = int(R56_3 // 2**9)
            if r6 <= 100 and R56_3 - r6 * 2**9 == 0 and sum([r * Rn(i + 1, 180) for i, r in enumerate([r1, r2, r3, r4, r5, r6])]) % 2**63 == R52 % 2**63:
                print(r1, r2, r3, r4, r5, r6)
                print(sum([r * Rn(i + 1, 180) for i, r in enumerate([r1, r2, r3, r4, r5, r6])]))
                print(sum([r * Rn(i + 1, 56) for i, r in enumerate([r1, r2, r3, r4, r5, r6])]))
            r5 -= 1
        r4 -= 1
    r3 -= 1
