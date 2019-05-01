num_ring_types = 6

d1 = 56
d2 = 180

Rd1 = [2**int(d1 // (i + 1)) for i in range(num_ring_types)]
Rd2 = [2**int(d2 // (i + 1)) for i in range(num_ring_types)]

T, W = [int(i) for i in input().split()]

for T in range(T):
    print(d1, flush=True)
    R1 = int(input())
    print(d2, flush=True)
    R2 = int(input())

    R = [0] * num_ring_types

    R[0] = int(R1 // Rd1[0])
    R1 -= R[0] * Rd1[0]
    R[1] = int(R1 // Rd1[1])
    R1 -= R[1] * Rd1[1]
    R[2] = int(R1 // Rd1[2])
    done = False
    while R[2] >= 0:
        R1_1 = R1 - R[2] * Rd1[2]
        R[3] = int(R1_1 // Rd1[3])
        while R[3] >= 0:
            R1_2 = R1_1 - R[3] * Rd1[3]
            R[4] = int(R1_2 // Rd1[4])
            while R[4] >= 0:
                R1_3 = R1_2 - R[4] * Rd1[4]
                R[5] = int(R1_3 // Rd1[5])
                if sum([r * rd for r, rd in zip(R, Rd2)]) % 2**63 == R2:
                    done = True
                if done:
                    break
                R[4] -= 1
            if done:
                break
            R[3] -= 1
        if done:
            break
        R[2] -= 1
    print(" ".join(str(r) for r in R))
    result = input()
    if result == "-1":
        exit()

