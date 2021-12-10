# import numpy as np
#
# with open('input9') as f:
#     lines = f.readlines()
#
# matrix = []
# for line in lines:
#     matrix.append([])
#     for c in line.strip():
#         matrix[-1].append(int(c))
# matrix = np.array(matrix)
#
# h,w = matrix.shape
# cumsum = 0
# for i in range(h):
#     for j in range(w):
#         if i > 0 and matrix[i-1,j] <= matrix[i,j]:
#             continue
#         if i < h - 1 and matrix[i+1,j] <= matrix[i,j]:
#             continue
#         if j > 0 and matrix[i,j-1] <= matrix[i,j]:
#             continue
#         if j < w - 1 and matrix[i,j+1] <= matrix[i,j]:
#             continue
#         cumsum += matrix[i,j] + 1
#         print((i,j))
# print(cumsum)

import numpy as np

def get_adjacent(r,c,h,w):
    adj = []
    if r > 0:
        adj.append((r-1,c))
    if r < h - 1:
        adj.append((r+1,c))
    if c > 0:
        adj.append((r,c-1))
    if c < w - 1:
        adj.append((r,c+1))
    return adj

def bfs_basin(bfs_record, r, c, h, w):
    size = 0
    adj = get_adjacent(r,c,h,w)

    if bfs_record[r,c]:
        return 0
    bfs_record[r,c] = True

    for (ra,ca) in adj:
        size += bfs_basin(bfs_record, ra, ca, h, w)

    return 1 + size

with open('input9') as f:
    lines = f.readlines()

matrix = []
for line in lines:
    matrix.append([])
    for c in line.strip():
        matrix[-1].append(int(c))
matrix = np.array(matrix)
bfs_record = np.zeros(shape=matrix.shape, dtype=np.bool)
bfs_record[matrix == 9] = True

h,w = matrix.shape
basin_sizes = []

for r in range(h):
    for c in range(w):
        if bfs_record[r,c]:
            continue

        basin_sizes.append(bfs_basin(bfs_record, r, c, h, w))

basin_sizes = sorted(basin_sizes)[::-1]
print(basin_sizes[0] * basin_sizes[1] * basin_sizes[2])

