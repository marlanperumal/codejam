from collections import defaultdict
from itertools import islice

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

prime_list = list(islice(primes(), 27))[1:]

cypher = {chr(i + 65): c for i, c in enumerate(prime_list)}

def encrypt(message):
    encoded = [cypher[c] for c in message]

    encrypted = []
    for i in range(len(message) - 1):
        encrypted.append(encoded[i] * encoded[i + 1])

    return encrypted

print("CJQUIZKNOWBEVYOFDPFLUXALGORITHMS", encrypt("CJQUIZKNOWBEVYOFDPFLUXALGORITHMS"))
print("ABAC", encrypt("ABAC"))