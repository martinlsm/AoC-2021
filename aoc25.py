import numpy as np

def deep_copy(lines):
    return [[c for c in line] for line in lines]

with open('input25') as f:
    lines = [list(line.strip()) for line in f.readlines()]

next = deep_copy(lines)
rounds = 0

changed = True
while changed:
    rounds += 1
    next = deep_copy(lines)
    changed = False

    for r in range(len(lines)):
        for c in range(len(lines[0])):
            c_next = (c + 1) % len(lines[0])
            if lines[r][c] == '>' and lines[r][c_next] == '.':
                next[r][c] = '.'
                next[r][c_next] = '>'
                changed = True

    lines = next
    next = deep_copy(lines)

    for r in range(len(lines)):
        for c in range(len(lines[0])):
            r_next = (r + 1) % len(lines)
            if lines[r][c] == 'v' and lines[r_next][c] == '.':
                next[r][c] = '.'
                next[r_next][c] = 'v'
                changed = True

    lines = next


print(rounds)
