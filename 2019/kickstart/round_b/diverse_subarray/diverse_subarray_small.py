from collections import defaultdict


def run(N, S, trinkets):
    max_trinkets = []
    for i in range(N):
        max_trinkets.append(0)
        trinket_count = defaultdict(int)
        num_trinkets = 0
        for trinket in trinkets[i:]:
            trinket_count[trinket] += 1
            if trinket_count[trinket] <= S:
                num_trinkets += 1
                max_trinkets[-1] = max(max_trinkets[-1], num_trinkets)
            elif trinket_count[trinket] == S + 1:
                num_trinkets -= S
    return max(max_trinkets)


if __name__ == "__main__":
    T = int(input())
    for t in range(1, T + 1):
        N, S = [int(i) for i in input().split()]
        trinkets = [int(i) for i in input().split()]
        result = run(N, S, trinkets)
        print("Case #{}: {}".format(t, result))
