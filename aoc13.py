import numpy as np

def print_points(points):
    hi_x = max([p[0] for p in points]) + 1
    hi_y = max([p[1] for p in points]) + 1
    for y in range(hi_y):
        for x in range(hi_x):
            if [x,y] in points:
                print('#', end='')
            else:
                print(' ', end='')
        print('')


def fold(points, axis, where):
    if axis == 'x':
        n = 0
    elif axis == 'y':
        n = 1
    print(f'axis = {axis}')
    print(f'where = {where}')

    for p in points:
        print(p)
        if axis == 'x' and p[0] > where:
            p[0] = 2 * where - p[0]
        elif axis == 'y' and p[1] > where:
            p[1] = 2 * where - p[1]
        print(p)

    points = [p for p in points if p[n] != where]


with open('input13') as f:
    lines = f.readlines()

state = 0
points = []
folds = []
for line in lines:
    line = line.strip()
    if line == '':
        state = 1
        continue

    if state == 0:
        x,y = line.split(',')
        x = int(x)
        y = int(y)
        points.append([x,y])

    elif state == 1:
        axis,where = line.split('=')
        axis = axis[-1]
        where = int(where)
        folds.append((axis,where))

for f in folds:
    fold(points, f[0], f[1])

unique = set()
for p in points:
    unique.add(tuple(p))

print(len(unique))

print_points(points)
