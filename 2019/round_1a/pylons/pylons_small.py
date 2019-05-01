from random import shuffle

def index_to_rc(i, R, C):
    return [int(i // C), i % C]

def rc_to_index(r, c, R, C):
    return r * C + c

def run(R, C):
    # This will probably require some input arguments
    visited = set()
    done = False
    cells = list(range(R*C))
    while not done:
        shuffle(cells)
        done = True
        tour = []
        for i in cells:
            r, c = index_to_rc(i, R, C)
            for j in visited:
                r1, c1 = index_to_rc(j, R, C)
                if r == r1 or c == c1 or r + c == r1 + c1 or r - c == r1 - c1:
                    done = False
                    break
            if not done:
                break
            tour.append(i)
                    
    result = "\n".join([" ".join([str(j) for j in index_to_rc(i, R, C)]) for i in tour])
    return result

if __name__ == "__main__":
    T = int(input())
    for t in range(1, T + 1):
        # There will probably be some additional inputs
        R, C = [int(i) for i in input().split()]
        result = run(R, C)
        print("Case #{}: {}".format(t, result))