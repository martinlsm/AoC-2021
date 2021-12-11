import numpy as np

# last = -1
# num_inc = -1
# 
# with open('input') as f:
#     lines = f.readlines()
#     for line in lines:
#         x = int(line)
#         if x > last:
#             num_inc += 1
#         last = x
# 
# print(num_inc)

num_inc = -1
last = -1

with open('input') as f:
    lines = f.readlines()
    data = (int(lines[i-2]) + int(lines[i-1]) + int(lines[i]) for i in range(2,len(lines)))

    for x in data:
        if x > last:
            num_inc += 1
        last = x

print(num_inc)
