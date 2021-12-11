import numpy as np

matrix = np.zeros(shape=(1000, 1000), dtype=np.uint64)

def parse_line(line):
    points = line.split(' -> ')
    points = [tuple(int(x) for x in p.split(',')) for p in points]
    return points

def line_points(points):
    [(x0,y0),(x1,y1)] = points
    min_y = min(y0, y1)
    max_y = max(y0, y1)
    min_x = min(x0, x1)
    max_x = max(x0, x1)
    if x0 == x1:
        return [(x0, y) for y in range(min_y, max_y + 1)]
    elif y0 == y1:
        return [(x, y0) for x in range(min_x, max_x + 1)]
    elif abs(x0 - x1) == abs(y0 - y1):
        step_x = 1 if x1 > x0 else -1
        step_y = 1 if y1 > y0 else -1
        x,y = x0,y0
        result = []
        while True:
            if x == x1 + step_x and y == y1 + step_y:
                break
            if x == x1 + step_x:
                raise ValueError('bad input')
            if y == y1 + step_y:
                raise ValueError('bad input')
            result.append((x,y))
            x += step_x
            y += step_y
        return result
    else:
        return None

def num_overlapping_lines(matrix):
    result = 0
    for x in range(matrix.shape[0]):
        for y in range(matrix.shape[1]):
            if matrix[x,y] > 1:
                result += 1

    return result



with open('test5', 'r') as f:
    lines = [l.strip() for l in f.readlines()]
    for line in lines:
        points = parse_line(line)
        points = line_points(points)
        if points is None:
            continue

        for (x,y) in points:
            matrix[x,y] += 1

    print(num_overlapping_lines(matrix))
