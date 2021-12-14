import numpy as np
import collections
from collections import defaultdict

with open('input14') as f:
    lines = f.readlines()

polymer = lines[0].strip()
insertion_rules = {}
print(polymer)

for line in lines[2:]:
    f,t = line.strip().split(' -> ')
    insertion_rules[f] = t

polymer_pairs = {}
for i in range(len(polymer) - 1):
    p = polymer[i:i+2]
    if p not in polymer_pairs:
        polymer_pairs[p] = 1
    else:
        polymer_pairs[p] += 1

count = defaultdict(lambda : 0)
for c in polymer:
    count[c] += 1
print(count)

for i in range(40):
    next_polymer_pairs = {}
    print(f'i = {i}')
    for p in polymer_pairs:
        print(p)
        in_between = insertion_rules[p]
        p0 = p[0] + in_between
        p1 = in_between + p[1]

        if p0 not in next_polymer_pairs:
            next_polymer_pairs[p0] = 0
        if p1 not in next_polymer_pairs:
            next_polymer_pairs[p1] = 0

        next_polymer_pairs[p0] += polymer_pairs[p]
        next_polymer_pairs[p1] += polymer_pairs[p]

        count[in_between] += polymer_pairs[p]

    polymer_pairs = next_polymer_pairs
    print(next_polymer_pairs)

hi = 0
lo = np.inf
for c in count:
    if count[c] > hi:
        hi = count[c]
    if count[c] < lo:
        lo = count[c]


print(count)
print(hi - lo)
