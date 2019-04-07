T = int(input())

for t in range(1, T + 1):
    N, P = [int(i) for i in input().split()]
    S = sorted([int(i) for i in input().split()])
    min_training = max(S) * P
    team_skill = sum(S[:P])
    for i in range(N - P + 1):
        if i > 0:
            team_skill += S[i + P - 1] - S[i - 1]
        training = S[i + P - 1] * P - team_skill
        if training < min_training:
            min_training = training
    print("Case #{}: {}".format(t, min_training))