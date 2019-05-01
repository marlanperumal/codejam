from collections import defaultdict


def run(N, S, trinkets):
    # trinket_types = set(trinkets)
    # trinket_counts = {
    #     trinket: [0] for trinket in trinket_types
    # }
    # for trinket in trinkets:
    #     for trinket_type in trinket_types:
    #         if trinket == trinket_type:
    #             trinket_counts[trinket_type]\
    #                 .append(trinket_counts[trinket_type][-1] + 1)
    #         else:
    #             trinket_counts[trinket_type]\
    #                 .append(trinket_counts[trinket_type][-1])
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
            # num_trinkets = sum([
            #     trinket_counts[t][j] - trinket_counts[t][i] 
            #     for t in trinket_types
            #     if trinket_counts[t][j] - trinket_counts[t][i] <= S
            # ])
            # max_trinkets = max(max_trinkets, num_trinkets)
    return max(max_trinkets)


if __name__ == "__main__":
    T = int(input())
    for t in range(1, T + 1):
        N, S = [int(i) for i in input().split()]
        trinkets = [int(i) for i in input().split()]
        result = run(N, S, trinkets)
        print("Case #{}: {}".format(t, result))
