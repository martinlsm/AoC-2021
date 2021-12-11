# x = 0
# y = 0
# 
# with open('input2', 'r') as f:
#     lines = f.readlines()
#     for line in lines:
#         line = line.split(' ')
# 
#         if line[0] == 'forward':
#             x += int(line[1])
#         elif line[0] == 'down':
#             y += int(line[1])
#         elif line[0] == 'up':
#             y -= int(line[1])
#         else:
#             raise ValueError('Unknown command')
# 
#     print(x * y)

x = 0
y = 0
aim = 0
with open('input2', 'r') as f:
    lines = f.readlines()
    for line in lines:
        line = line.split(' ')

        if line[0] == 'forward':
            y += int(line[1]) * aim
            x += int(line[1])
        elif line[0] == 'down':
            aim += int(line[1])
        elif line[0] == 'up':
            aim -= int(line[1])
        else:
            raise ValueError('Unknown command')

    print(x * y)
