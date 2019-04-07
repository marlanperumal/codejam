from math import log2, ceil
import sys

T = int(input())

for t in range(1, T + 1):
    N, B, F = [int(i) for i in input().split()]
    levels = ceil(log2(N))
    requests = []
    responses = []
    fail = False

    for level in range(min(levels, F)):
        request = ""
        bit = "0"
        while len(request) < N:
            request += bit * (2**level)
            bit = "1" if bit == "0" else "0"
        request = request[:N]
        requests.append(request)
        print(request)
        sys.stdout.flush()
        response = input()
        if response == "-1":
            fail = True
            break
        responses.append([c for c in response])
    if fail:
        break

    keys = [[request[i] for request in requests] for i in range(N)]
    response_keys = [[response[i] for response in responses] for i in range(N - B)]

    broken = []
    response_id = 0
    for i, key in enumerate(keys):
        if response_id == N - B or key != response_keys[response_id]:
            broken.append(i)
        else:
            response_id += 1
    print(" ".join([str(i) for i in broken]))
    sys.stdout.flush()
    verdict = input()
    if verdict != "1":
        break




