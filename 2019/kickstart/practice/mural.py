T = int(input())

for t in range(1, T + 1):
    N = int(input())
    beauty_points = [int(i) for i in input()]

    k = int((N + 1) // 2)
    score = sum(beauty_points[:k])
    highest_score = score
    for i in range(N - k):
        score += beauty_points[i + k] - beauty_points[i]
        if score > highest_score:
            highest_score = score

    print("Case #{}: {}".format(t, highest_score))