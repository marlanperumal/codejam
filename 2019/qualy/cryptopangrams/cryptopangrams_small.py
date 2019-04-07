from collections import defaultdict

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

T = int(input())

for t in range(1, T + 1):
    N, L = [int(i) for i in input().split()]
    ciphertext = [int(i) for i in input().split()]

    for p1 in primes():
        if ciphertext[0] % p1 == 0:
            break
    p2 = ciphertext[0] // p1

    encrypted_message = [p1, p2]
    p = p2
    redo = False

    for c in ciphertext[1:]:
        p = c / p
        if p != int(p):
            redo = True
            break
        encrypted_message.append(p)

    if redo:
        p1, p2 = p2, p1
        encrypted_message = [p1, p2]
        p = p2

        for c in ciphertext[1:]:
            p = c / p
            encrypted_message.append(p)

    cypher = {c: chr(i + 65) for i, c in enumerate(sorted(set(encrypted_message)))}
    message = [cypher[c] for c in encrypted_message]

    print("Case #{}: {}".format(t, "".join(message)))

