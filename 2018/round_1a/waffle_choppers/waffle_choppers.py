T = int(input())
for t in range(1, T+1):
    R, C, H, V = [int(si) for si in input().split()]
    grid = []
    for r in range(R):
        grid.append([1 if ri == "@" else 0 for ri in str(input())])
    # print(grid)
    chocs = sum([sum(row) for row in grid])

    done = False

    if chocs % ((H+1)*(V+1)) == 0:
        chocs_each = chocs / ((H+1)*(V+1))
        for r in range(1,R):
            impossible = False
            if not impossible:


                top = grid[:r]
                # print(top)

                for c in range(1,C):
                    sum_chocs = sum([sum(row[:c]) for row in top])
                    # print(c, sum_chocs)
                    if sum_chocs == chocs_each:
                        hcuts = [r]
                        vcuts = []
                        top = [row[c:] for row in top]
                        bottom = [row[:c] for row in grid[r:]]
                        vcuts.append(c)
                        for v in range(V-1):
                            left_cell = vcuts[-1]
                            right_cell = vcuts[-1]

                        vcuts = [0] + vcuts + [C+1]
                        hcuts = [0] + hcuts + [R+1]
                        waffles = []
                        for hi in range(len(hcuts)-1):
                            for vi in range(len(vcuts)-1):
                                waffles.append([row[vcuts[vi]:vcuts[vi+1]] for row in grid[hcuts[hi]:hcuts[hi+1]]])
                        # print(vcuts)
                        # print(hcuts)
                        # print(waffles)
                        waffle_chocs = [
                            sum([sum(row) for row in waffle]) for waffle in waffles
                        ]
                        # print(waffle_chocs)
                        if all([waffle_choc == chocs_each for waffle_choc in waffle_chocs]):
                            done = True
                            break
                        # break
                    elif sum_chocs > chocs_each:
                        impossible = True
                        break
                # if impossible:
                #     break


    # ans = [R, C, H, V]
    ans = "POSSIBLE" if done else "IMPOSSIBLE"
    print("Case #{}: {}".format(t, ans))
    # print(grid)
