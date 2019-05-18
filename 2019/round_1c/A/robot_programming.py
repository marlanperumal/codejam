from collections import deque
# input_file = "robot_testing.sample.in"


# def input_from_file(filename):
#     for line in open(filename):
#         yield line.strip()


# file_input = input_from_file(input_file)


# def input():
#     return next(file_input)





class Turn():
    def __init__(self, turn_num, move, opponents, parent):
        self.turn_num = turn_num
        self.move = move
        self.opponents = opponents
        self.parent = parent
        # print(turn_num, move, opponents)

    def eval_move(self):
        global queue
        if self.turn_num > 900:
            return False
        global overall_winner
        remaining_opponents = []
        for opponent in self.opponents:
            opp_move = opponent[self.turn_num % len(opponent)]
            if self.move == opp_move:
                remaining_opponents.append(opponent)
            elif (self.move == "R" and opp_move == "P") \
                    or (self.move == "P" and opp_move == "S") \
                    or (self.move == "S" and opp_move == "R"):
                return False
            elif (self.move == "P" and opp_move == "R") \
                    or (self.move == "S" and opp_move == "P") \
                    or (self.move == "R" and opp_move == "S"):
                pass
        if len(remaining_opponents) > 0:
            for move in "RPS":
                turn = Turn(self.turn_num + 1, move, remaining_opponents, self)
                queue.append(turn)
            return False
                
        else:
            overall_winner = self
            return True

    def get_strategy(self):
        if self.parent is None:
            return self.move
        else:
            return self.parent.get_strategy() + self.move


def run(A, C):
    for move in "RPS":
        turn = Turn(0, move, C, None)
        queue.append(turn)
    while queue:
        turn = queue.popleft()
        result = turn.eval_move()
        if result:
            return overall_winner.get_strategy()
    return "IMPOSSIBLE"


if __name__ == "__main__":
    T = int(input())
    for t in range(1, T + 1):
        overall_winner = None
        queue = deque()
        A = int(input())
        C = [input() for a in range(A)]
        result = run(A, C)
        print("Case #{}: {}".format(t, result))
