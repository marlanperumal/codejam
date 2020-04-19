# input_file = "pattern_matching.in"


# def input_from_file(filename):
#     for line in open(filename):
#         yield line.strip()


# file_input = input_from_file(input_file)


# def input():
#     return next(file_input)


def run(P):
    Pl = [p.split("*") for p in P]
    for i, p in enumerate(P):
        if p.startswith("*"):
            Pl[i] = [""] + Pl[i]
        if p.endswith("*"):
            Pl[i] = Pl[i] + [""]
    L = []
    R = []
    while any(Pl):
        l = []
        r = []
        for p in Pl:
            if len(p) > 0:
                l.append(p.pop(0))
            else:
                l.append("")
            if len(p) > 0:
                r.append(p.pop())
            else:
                r.append("")
        L.append(l)
        R.append(r)

    ll = ""
    rr = ""
    for l, r in zip(L, R):
        l = sorted(l, key=lambda s: len(s), reverse=True)
        r = sorted(r, key=lambda s: len(s), reverse=True)
        for i in range(1, len(l)):
            if not l[i - 1].startswith(l[i]):
                return "*"
        for i in range(1, len(r)):
            if not r[i - 1].endswith(r[i]):
                return "*"
        ll = ll + l[0]
        rr = r[0] + rr
    return ll + rr


if __name__ == "__main__":
    T = int(input())
    for t in range(1, T + 1):
        N = int(input())
        P = [input() for i in range(N)]
        result = run(P)
        print("Case #{}: {}".format(t, result))