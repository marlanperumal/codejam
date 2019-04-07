def training(N, P, S):

    # min_training = max(S) * P
    # team_skill = sum(S[:P])
    # for i in range(N - P + 1):
    #     if i > 0:
    #         team_skill += S[i + P - 1] - S[i - 1]
    #     training = max(S[i:i + P]) * P - team_skill
    #     if training < min_training:
    #         min_training = training

    min_training = max(S) * P
    team_skill = sum(S[:P])
    for i in range(N - P + 1):
        if i > 0:
            team_skill += S[i + P - 1] - S[i - 1]
        training = max(S[i:i + P]) * P - team_skill
        if training < min_training:
            min_training = training
    return min_training

# T = int(input())

# for t in range(1, T + 1):
#     N, P = [int(i) for i in input().split()]
#     S = sorted([int(i) for i in input().split()])
#     min_training = training(N, P, S)
#     print("Case #{}: {}".format(t, min_training))

import random
N = int(10**5)
P = int(10**3)
S = [random.randint(0, 10000) for i in range(N)]
print(training(N, P, S))