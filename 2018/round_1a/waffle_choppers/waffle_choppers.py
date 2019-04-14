T = int(input())

for t in range(1, T + 1):
    R, C, H, V = [int(i) for i in input().split()]
    grid = [
        [1 if c == '@' else 0 for c in input()] for r in range(R)
    ]
    total_chips = sum([sum(row) for row in grid])
    chips_per_vertical = total_chips / (V + 1)
    chips_per_horizontal = total_chips / (H + 1)
    chips_per_piece = total_chips / (V + 1) / (H + 1)

    if total_chips == 0:
        result = "POSSIBLE"
    elif int(chips_per_piece) != chips_per_piece:
        result = "IMPOSSIBLE"
    else:
        h_cuts = [0]
        v_cuts = [0]
        complete_rows = 0
        row_count = 0
        for r, row in enumerate(grid):
            row_count += sum(row)
            if row_count == chips_per_horizontal:
                complete_rows += 1
                row_count = 0
                h_cuts.append(r + 1)
            elif row_count > chips_per_horizontal:
                break
        complete_cols = 0
        col_count = 0
        for c in range(C):
            col_count += sum([row[c] for row in grid])
            if col_count == chips_per_vertical:
                complete_cols += 1
                col_count = 0
                v_cuts.append(c + 1)
            elif col_count > chips_per_vertical:
                break
        if complete_rows != H + 1 or complete_cols != V + 1:
            result = "IMPOSSIBLE"
        else:
            possible = True
            for r in range(H):
                if not possible:
                    break
                for c in range(V):
                    chips = sum([sum(row[v_cuts[c]:v_cuts[c+1]]) 
                        for row in grid[h_cuts[r]:h_cuts[r+1]]])
                    if chips != chips_per_piece:
                        possible = False
                        break
            if not possible:
                result = "IMPOSSIBLE"
            else:
                result = "POSSIBLE"

    print("Case #{t}: {result}".format(t=t, result=result))
