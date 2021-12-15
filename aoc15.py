import numpy as np

def find_lowest_cost(costs, visited):
    lo = np.inf
    res = None
    for i in range(costs.shape[0]):
        for j in range(costs.shape[1]):
            if costs[i,j] < lo and (i,j) not in visited:
                res = (i,j)
                lo = costs[i,j]
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




with open('input15') as f:
    lines = f.readlines()

matrix = []

for line in lines:
    matrix.append([])
    for c in line.strip():
        matrix[-1].append(int(c))

matrix = np.array(matrix)
costs = np.empty(shape=matrix.shape)
costs.fill(np.inf)
costs[0,0] = 0
visited = set()

H = matrix.shape[0]
W = matrix.shape[1]

prev = [[(-1,-1) for _ in range(W)] for _ in range(H)]

while True:
    lowest = find_lowest_cost(costs, visited)
    if lowest is not None:
        (r,c) = lowest
    else:
        break
    if (r,c) == (H - 1,W - 1):
        break
    visited.add((r,c))

    neighbours = find_neighbours(r,c,H,W)

    for (nr,nc) in neighbours:
        if costs[nr,nc] > costs[r,c] + matrix[nr,nc]:
            costs[nr,nc] = costs[r,c] + matrix[nr,nc]
            prev[nr][nc] = (r,c)
