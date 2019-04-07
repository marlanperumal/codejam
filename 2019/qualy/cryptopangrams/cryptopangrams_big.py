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

T = int(input())

for t in range(1, T + 1):
    N, L = [int(i) for i in input().split()]
    ciphertext = [int(i) for i in input().split()]

    for i in range(len(ciphertext)):
        if ciphertext[i] != ciphertext[i+1]:
            break

    p1 = gcd(ciphertext[i], ciphertext[i+1])
    encrypted_message = [p1]
    p = p1
    for c in reversed(ciphertext[:i+1]):
        p = int(c // p)
        encrypted_message.append(p)
    encrypted_message = [p for p in reversed(encrypted_message)]
    p = p1
    for c in ciphertext[i+1:]:
        p = int(c // p)
        encrypted_message.append(p)

    cypher = {c: chr(i + 65) for i, c in enumerate(sorted(set(encrypted_message)))}
    message = [cypher[c] for c in encrypted_message]

    print("Case #{}: {}".format(t, "".join(message)))

