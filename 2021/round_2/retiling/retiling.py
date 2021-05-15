class Tile():
    def __init__(self, R, C, i, j, c, swappable):
        self.i = i
        self.j = j
        self.c = c
        self.neighbours = set()
        self.swappable_neighbours = set()
        self.swappable = swappable

    def add_neighbour(self, neighbour):
        self.neighbours.add(neighbour)
        neighbour.neighbours.add(self)
        if self.swappable and neighbour.swappable and self.c != neighbour.c:
            self.swappable_neighbours.add(neighbour)
            neighbour.swappable_neighbours.add(self)

    def __hash__(self):
        return self.i * C + self.j


def run(R, C, F, S, sg, tg):
    tiles = {}
    for r in range(R):
        for c in range(C):
            tile = Tile(R, C, r, c, sg[r][c], sg[r][c] != tg[r][c])
            tiles[(r, c)] = tile
            if r > 0:
                neighbour = tiles[(r-1, c)]
                tile.add_neighbour(neighbour)
            if c > 0:
                neighbour = tiles[(r, c-1)]
                tile.add_neighbour(neighbour)

    swappable_tiles = {tile for tile in tiles.values() if tile.swappable}

    flips = 0
    swaps = 0
    while swappable_tiles:
        tile = min(swappable_tiles, key=lambda t: len(t.swappable_neighbours))
        if len(tile.swappable_neighbours) > 0:
            neighbour = min(tile.swappable_neighbours, key=lambda n: len(n.swappable_neighbours))
            for neighbour in tile.swappable_neighbours:
                neighbour.swappable_neighbours.remove(tile)
            for neighbour2 in neighbour.swappable_neighbours:
                neighbour2.swappable_neighbours.remove(neighbour)
            swappable_tiles.remove(tile)
            swappable_tiles.remove(neighbour)
            swaps += 1
        else:
            swappable_tiles.remove(tile)
            flips += 1
    cost = flips * F + swaps * S
    return cost


T = int(input())

for t in range(1, T + 1):
    R, C, F, S = [int(i) for i in input().split()]
    sg = [[c for c in input()] for _ in range(R)]
    tg = [[c for c in input()] for _ in range(R)]
    result = run(R, C, F, S, sg, tg)
    print(f"Case #{t}: {result}")
