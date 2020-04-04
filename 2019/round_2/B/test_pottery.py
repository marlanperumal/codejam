from random import randint
from collections import defaultdict

wins = 0
for t in range(250):
    vases = defaultdict(int)
    
    for d in range(1, 91):
        vases[randint(1, 20)] += 1
    
    vases[randint(1, 20)] += 1
    v19 = vases[19]
    vases[randint(1, 20)] += 1
    v20 = vases[20]
    if v20 <= v19:
        winner = 20
        loser = 19
    else:
        winner = 19
        loser = 20
    for d in range(93, 100):
        vases[randint(1, 20)] += 1
    for i in range(1, 19):
        vases[i] += 5
    vases[loser] += 7
    vases[winner] += 1
    min_vase_weight = min(vases.values())
    lightest = [vase for vase in vases if vases[vase] == min_vase_weight]
    if len(lightest) == 1 and lightest[0] == winner:
        wins += 1
    else:
        print([vases[vase] for vase in sorted(vases)])

print(wins)
