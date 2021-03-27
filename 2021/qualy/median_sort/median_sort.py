def list2str(L):
    return " ".join([str(i) for i in L])


def partition(L, q):
    if len(L) < 3:
        return L, q
    i, j, k = L[0], L[1], L[2]
    q += 1
    # if q > Q:
    #     exit()
    print(list2str([i, j, k]))
    m = int(input())
    if m == i:
        i, j = j, i
    elif m == k:
        j, k = k, j
    if len(L) == 3:
        return [i, j, k], q

    Ll = [i]
    Lr = [j, k]
    for k in L[3:]:
        q += 1
        # if q > Q:
        #     exit()
        print(list2str([i, j, k]))
        m = int(input())
        if m == i:
            i, k = k, i
            Ll = [i] + Ll
        elif m == j:
            Lr.append(k)
        elif m == k:
            Ll.append(k)
    Ll, q = partition(Ll, q)
    Lr, q = partition(Lr, q)
    return Ll + Lr, q


def run(N, q):
    L = list(range(1, N + 1))
    return partition(L, q)


T, N, Q = [int(i) for i in input().split()]
q = 0

for t in range(1, T + 1):
    result, q = run(N, q)
    print(list2str(result))
    response = int(input())
    if response == -1:
        exit()
