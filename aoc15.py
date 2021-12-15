import numpy as np

class Node():
    def __init__(self, r, c, H, W):
        self.r = r
        self.c = c
        self.h = np.abs(r - (H - 1)) + np.abs(c - (W - 1))
        #self.h = 0
        self.g = np.inf
        self.prev = None

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f'Node({self.r,self.c})'

    def __hash__(self):
        return hash((self.r, self.c))

    def __eq__(self, other):
        return self.r == other.r and self.c == other.c

def find_lowest_cost(open_nodes):
    lo = np.inf
    res = None
    for node in open_nodes:
        if node.g + node.h < lo:
            lo = node.g + node.h
            res = node
    return res


def inside(r,c,H,W):
    return r >= 0 and c >= 0 and r < H and c < W

def find_neighbours(r,c,H,W):
    neighbours = []
    if inside(r - 1, c, H, W):
        neighbours.append((r - 1, c))
    if inside(r, c - 1, H, W):
        neighbours.append((r, c - 1))
    if inside(r + 1, c, H, W):
        neighbours.append((r + 1, c))
    if inside(r, c + 1, H, W):
        neighbours.append((r, c + 1))
    return neighbours


def get_elem(matrix, r, c):
    rmod = r % matrix.shape[0]
    cmod = c % matrix.shape[1]
    val = matrix[rmod,cmod]
    rr = r // matrix.shape[0]
    cc = c // matrix.shape[1]
    return ((val - 1 + rr + cc) % 9) + 1


with open('input15') as f:
    lines = f.readlines()

matrix = []

for line in lines:
    matrix.append([])
    for c in line.strip():
        matrix[-1].append(int(c))

matrix = np.array(matrix)

H = 5 * matrix.shape[0]
W = 5 * matrix.shape[1]

start = Node(0,0,H,W)
start.g = 0
nodes = {}
nodes[(0,0)] = start
open_nodes = set([start])

end = None
while True:
    node = find_lowest_cost(open_nodes)
    assert node is not None

    if node.r == H - 1 and node.c == W - 1:
        end = node
        break

    open_nodes.remove(node)

    neighbours = find_neighbours(node.r,node.c,H,W)
    for (nr,nc) in neighbours:
        if (nr,nc) not in nodes:
            nodes[(nr,nc)] = Node(nr,nc,H,W)

        edge_cost = get_elem(matrix, nr, nc)
        tentative_cost = node.g + edge_cost
        if tentative_cost < nodes[(nr,nc)].g:
            nodes[(nr,nc)].g = tentative_cost
            nodes[(nr,nc)].prev = node
            if nodes[(nr,nc)] not in open_nodes:
                open_nodes.add(nodes[(nr,nc)])


print(end.g)
