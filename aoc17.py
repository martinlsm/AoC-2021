import numpy as np

def will_hit(x_i, y_i, x_t0, x_t1, y_t0, y_t1):
    loc = (0,0)
    while loc[1] >= y_t0 and loc[0] <= x_t1:
        loc = (loc[0] + x_i, loc[1] + y_i)
        x_i = max(0, x_i - 1)
        y_i = y_i - 1

        if loc[0] >= x_t0 and loc[0] <= x_t1 and loc[1] >= y_t0 and loc[1] <= y_t1:
            return True
    return False

with open('input17') as f:
    line = f.readlines()[0].strip()

d0 = line.index('x=')
line = line[d0:]

d0 = line.index('..')
d1 = line.index(',')
d2 = line.index('y=')
x_t0 = int(line[2:d0])
x_t1 = int(line[d0+2:d1])
line = line[d2:]

d0 = line.index('..')
y_t0 = int(line[2:d0])
y_t1 = int(line[d0+2:])

# Solve part 1
ya = np.abs(y_t0)
max_y = (ya - 1) * ya // 2
print(max_y)

# Sovle part 2
high_y = 90
low_y = y_t0
high_x = x_t1 + 1
low_x = 0
count = 0
for x_i in range(low_x, high_x):
    for y_i in range(low_y, high_y):
        if will_hit(x_i, y_i, x_t0, x_t1, y_t0, y_t1):
            count += 1

print(count)
