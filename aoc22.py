import numpy as np
import re

xs = []
ys = []
zs = []

def reduce(l):
    p0 = 0
    

with open('test22') as f:
    lines = f.readlines()

for line in lines[:3]:
    line = line.strip()

    mode = line[:line.index(' ')]
    position = [int(x) for x in re.findall('[-]?\d+', line)]

    if mode == 'on':
        xs.append([position[0], position[1]])
    else:
        new_xs = []
        for x in xs:

            if position[0] <= x[0] and position[1] < x[1]:
                new_x = x.copy()
                new_x[0] = position[1] + 1
                new_xs.append(new_x)
            elif position[1] >= x[1] and position[0] > x[1]:
                new_x = x.copy()
                new_x[1] = position[0] - 1
                new_xs.append(new_x)
            elif position[0] > x[0] and position[1] < x[1]:
                new_x1 = [x[0], position[0] - 1]
                new_x2 = [position[1] + 1, x[1]]
                new_xs.append(new_x1)
                new_xs.append(new_x2)
            elif position[0] <= x[0] and position[1] >= x[1]:
                pass
            else:
                new_x = x.copy()
                new_xs.append(new_x)

            new_xs.append(position)
        print(new_xs)


print(xs) 
    
