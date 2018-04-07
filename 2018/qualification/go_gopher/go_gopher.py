from math import sqrt
import sys

def ij2n(I, J, i, j):
    if i >=0 and i < I and j >= 0 and j < J:
        return i*J + j
    else:
        return I*J

def n2ij(I, J, n):
    if n >=0 and n < I*J:
        i = n//J
        j = n % J
        return i, j
    else:
        return I, J

class Cell():
    def __init__(self, I, J, n):
        self.I = I
        self.J = J
        self.n = n
        i, j = n2ij(I, J, n)
        self.i = i
        self.j = j
        neighbours = [
            ij2n(I, J, i-1, j-1),
            ij2n(I, J, i-1, j),
            ij2n(I, J, i-1, j+1),
            ij2n(I, J, i, j+1),
            ij2n(I, J, i+1, j+1),
            ij2n(I, J, i+1, j),
            ij2n(I, J, i+1, j-1),
            ij2n(I, J, i, j-1)
        ]
        self.neighbours = [
            neighbour for neighbour in neighbours if neighbour < I*J
        ]
        self.prepared = False
        self.unprepared_neighbours = len(self.neighbours)

def unprepared_neighbours(cell):
    return cell.unprepared_neighbours

def is_inner_cell(cell):
    i = cell.i
    j = cell.j
    I = cell.I
    J = cell.J
    return (i >0 and i < I-1 and j > 0 and j < J-1)

T = int(input())
error = False
for t in range(1, T+1):
    if error:
        break
    A = int(input())
    I, J = 0, 0
    complete = False

    if A == 20:
        I, J = 4, 5
    elif A == 200:
        I, J = 10, 20
    else:
        I = int(sqrt(20)) + 1
        J = int(sqrt(20)) + 1
    cells = {}
    for n in range(I*J):
        cells[n] = Cell(I, J, n)

    inner_cells = {
        cell.n: cell for cell in cells.values() \
            if is_inner_cell(cell)
    }

    while not complete:
        cell = max(inner_cells.values(), key=unprepared_neighbours)
        print(cell.i + 100, cell.j + 100)
        sys.stdout.flush()
        i, j = [int(si) for si in input().split()]
        if i == 0 and j == 0:
            complete = True
        elif i == -1 and j == -1:
            complete = True
            error = True
        else:
            i -= 100
            j -= 100
            n = ij2n(I, J, i, j)
            prep_cell = cells[n]
            if not prep_cell.prepared:
                prep_cell.prepared = True
                for neighbour in prep_cell.neighbours:
                    cells[neighbour].unprepared_neighbours -= 1
            # complete = all([cell.prepared for cell in cells.values()])
