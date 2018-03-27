def read_int():
    return int(input())

def read_int_list():
    return [int(n) for n in input().split(" ")]

def read_str():
    return input()

def read_char_list():
    return [c for c in input().split(" ")]

def write_case_ans(i,ans):
    if isinstance(ans,list):
        ans = " ".join(map(str, ans))
    print("Case #{}: {}".format(i, ans))

def main():
    T = read_int()
    for t in range(1, T+1):
        N, Q = read_int_list()
        E = []
        S = []
        D = []
        U = []
        V = []
        for n in range(N):
            e, s = read_int_list()
            E.append(e)
            S.append(s)
        for n in range(N):
            d = read_int_list()
            D.append(d)
        for q in range(Q):
            u, v = read_int_list()
            U.append(u)
            V.append(v)

        distances = [d[i+1] for i, d in enumerate(D[:-1])]
        routes = [[d for d in distances] for n in range(N-1)]

        # print(N, Q)
        # print(E)
        # print(S)
        # print(D)
        # print(distances)
        # print(routes)
        # print(U)
        # print(V)

        for i, (e, s) in enumerate(zip(E[:-1], S[:-1])):
            route = routes[i]
            for j, d in enumerate(distances[i:]):
                if e >= d:
                    route[j+i] = d/s
                    e -= d
                else:
                    break

        # print(routes)
        for i in range(N-2):
            ii = N - 2 - i
            r1 = routes[ii]
            quickest = r1[ii]
            for j in range(ii):
                jj = ii - j - 1
                r2 = routes[jj]
                if r2[ii] < quickest:
                    quickest = r2[ii]
                # else:
                #     r2[ii] = quickest
        # print(routes)
        for i in range(N-2):
            ii = i
            r1 = routes[ii]
            for j in range(N-i-2):
                jj = j + i + 1
                r2 = routes[jj]
                r2[ii] = r1[ii]
        # print(routes)

        route_sums = [sum(route) for route in routes]
        write_case_ans(t, min(route_sums))




if __name__ == "__main__":
    main()
