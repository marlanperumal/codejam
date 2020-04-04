T = int(input())
for t in range(T):
    players = set(list(range(1, 100)))
    for d in range(1, 101):
        current_day = int(input())
        if current_day != d:
            exit()
        if d <= 16:
            v = d % 16
            p = 100
            print(v + 1, p, flush=True)
        elif d <= 80:
            v = d % 16
            p = players.pop()
            print(v + 1, p, flush=True)
        elif d == 81:
            print(17, 0, flush=True)
            v17_1 = [int(i) for i in input().split()]
        elif d == 82:
            print(18, 0, flush=True)
            v18_1 = [int(i) for i in input().split()]
        elif d == 83:
            print(19, 0, flush=True)
            v19_1 = [int(i) for i in input().split()]
        elif d == 84:
            print(20, 0, flush=True)
            v20_1 = [int(i) for i in input().split()]
            players = players - set(v17_1) - set(v18_1) - set(v19_1) - set(v20_1)
            winners = [17, 18, 19, 20]
            min_count = min([len(v17_1), len(v18_1), len(v19_1), len(v20_1)])
            if len(v17_1) == min_count:
                winner = 17
            elif len(v18_1) == min_count:
                winner = 18
            elif len(v19_1) == min_count:
                winner = 19
            elif len(v20_1) == min_count:
                winner = 20
            losers = [loser for loser in winners if loser != winner]
        else:
            if d <= 87:
                j = d % 3
                v = losers[j]
                print(v, 100, flush=True)
            elif d < 100:
                j = d % 3
                v = losers[j]
                print(v, players.pop(), flush=True)
            else:
                print(winner, 100, flush=True)
