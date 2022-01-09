import numpy as np
from collections import defaultdict

def to_matrix(p, r0, r1, c0, c1):
    m = np.zeros(shape=(r1 - r0, c1 - c0), dtype=bool)
    for r in range(r0, r1):
        for c in range(c0, c1):
            if (r,c) in p:
                m[r - r0,c - r0] = True
    return m

def print_matrix(m):
    for r in range(len(m)):
        for c in range(len(m[0])):
            print('#' if m[r,c] else '.', end='')
        print('')
    print('\n\n')


with open('input20') as f:
    lines = [line.strip() for line in f.readlines()]

# top_str = '##...###...##.#..###.#...#....#..###.##.###...###.##.##.####.#######..######....#.###.##....#.##...#..........#####..##..#..##...##....####.###..#..####.##.##.#....#.##.#.#.#.#..##.##.#...##..##...#.#...#...#..#.#...#.##...#..######.#.##..#.#.#...##.###..########...........#.#.###.#.#..##...#..#..###..#..##.#.#...##..##..###..#####...#.####....#.###....###.##.##...##.#..#.#..####....#..##...##.#####.###.###.###.....##...#.#..#.######.##.##.......###...#.....#...##..#..#.###.#..#..########.##......###..##.#.'
top_str = lines[0]
print(top_str)

h0 = len(lines[2:])
w0 = len(lines[2])
pad = 100

matrix = np.zeros(shape=(h0+2*pad,w0+2*pad), dtype=bool)

for r,line in enumerate(lines[2:]):
    for c,e in enumerate(line):
        matrix[r+pad,c+pad] = (e == '#')

for i in range(50):
    print(i)
    next_matrix_vals = np.zeros(shape=matrix.shape, dtype=np.int64)
    for r in range(1,matrix.shape[0] - 1):
        for c in range(1, matrix.shape[1] - 1):
            next_matrix_vals[r,c] += (1 << 8) if matrix[r-1,c-1] else 0
            next_matrix_vals[r,c] += (1 << 7) if matrix[r-1,c]   else 0
            next_matrix_vals[r,c] += (1 << 6) if matrix[r-1,c+1] else 0
            next_matrix_vals[r,c] += (1 << 5) if matrix[r,c-1]   else 0
            next_matrix_vals[r,c] += (1 << 4) if matrix[r,c]     else 0
            next_matrix_vals[r,c] += (1 << 3) if matrix[r,c+1]   else 0
            next_matrix_vals[r,c] += (1 << 2) if matrix[r+1,c-1] else 0
            next_matrix_vals[r,c] += (1 << 1) if matrix[r+1,c]   else 0
            next_matrix_vals[r,c] += (1 << 0) if matrix[r+1,c+1] else 0

    next_matrix = np.zeros(shape=matrix.shape, dtype=bool)
    for r in range(0,len(next_matrix)):
        for c in range(0,len(next_matrix[0])):
            next_matrix[r,c] = (top_str[next_matrix_vals[r,c]] == '#')

    matrix = next_matrix

print_matrix(matrix)
print(np.sum(matrix[pad//2:-pad//2,pad//2:-pad//2]))



# points = set()
# for r,line in enumerate(lines[2:]):
#     for c,e in enumerate(line):
#         if e == '#':
#             points.add((r,c))
#         else:
#             assert e == '.'
# 
# for _ in range(2):
#     print(len(points))
#     next_points_vals = defaultdict(lambda: 0)
#     for r,c in points:
#         next_points_vals[(r - 1, c - 1)] += 1 << 0
#         next_points_vals[(r - 1, c)]     += 1 << 1
#         next_points_vals[(r - 1, c + 1)] += 1 << 2
#         next_points_vals[(r, c - 1)]     += 1 << 3
#         next_points_vals[(r, c)]         += 1 << 4
#         next_points_vals[(r, c + 1)]     += 1 << 5
#         next_points_vals[(r + 1, c - 1)] += 1 << 6
#         next_points_vals[(r + 1, c)]     += 1 << 7
#         next_points_vals[(r + 1, c + 1)] += 1 << 8
# 
# 
#     next_points = set()
#     for p,v in next_points_vals.items():
#         print('{}: {}', p, v)
#         assert v < (1 << 10)
#         if top_str[v] == '#':
#             next_points.add(p)
# 
#     points = next_points
#     print_matrix(to_matrix(points, -6, 10, -6, 10))
# 
# print(len(points))
