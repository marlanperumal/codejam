class Square():
    def __init__(self, r, c, R, C):
        self.R = R
        self.C = C
        self.r = r
        self.c = c
        self.knight_moves = [
            c1 + r1 * C for r1 in range(R) for c1 in range(C)
            if r != r1 and c != c1 and r - c != r1 - c1 and r + c != r1 + c1
        ]
        self.visited = False


class Board():
    def __init__(self, R, C):
        self.R = R
        self.C = C
        self.reset_board()
        

    def check_board(self):
        return len(self.visited) ==  R * C

    def next_move(self):
        lowest_onward = R * C
        possible_moves = []
        for possible_move in self.squares[self.current].knight_moves:
            if self.squares[possible_move].visited:
                continue
            square = self.squares[possible_move]
            valid_moves = []
            for knight_move in square.knight_moves:
                if not self.squares[knight_move].visited:
                    valid_moves.append(knight_move)
            if len(valid_moves) < lowest_onward:
                possible_moves = [possible_move]
            elif len(valid_moves) == lowest_onward:
                possible_moves.append(possible_move)
        if len(possible_moves) > 0:
            return possible_moves[0]
        else:
            return None

    def reset_board(self):
        self.squares = [
            Square(r, c, R, C) for r in range(self.R) for c in range(self.C)
        ]
        self.visited = []
        self.current = None

    def make_tour(self):
        move = int((self.C) // 2 + ((self.R) // 2) * self.C)
        while not self.check_board():  
            if move is not None:
                self.current = move
                self.visited.append(move)
                self.squares[move].visited = True
            else:
                return None
            move = self.next_move()
        return [[self.squares[i].r, self.squares[i].c] for i in self.visited]



def pylons(R, C):
    board = Board(R, C)
    tour = board.make_tour()
    if tour is None:
        return "IMPOSSIBLE"
    else:
        return "\n".join(["POSSIBLE"] + [
            "{} {}".format(move[0] + 1, move[1] + 1) for move in tour
        ])

    return result

if __name__ == "__main__":
    T = int(input())
    for t in range(1, T + 1):
        R, C = [int(i) for i in input().split()]
        result = pylons(R, C)
        print("Case #{}: {}".format(t, result))