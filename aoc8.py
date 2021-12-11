import numpy as np


def process_line(inputs, outputs):
    found_digits = dict()

    l = inputs.copy()

    # Find 1,4,7,8
    for num in inputs:
        if len(num) == 2:
            found_digits[num] = 1
            found_digits[1] = num
            l.remove(num)
        elif len(num) == 4:
            found_digits[num] = 4
            found_digits[4] = num
            l.remove(num)
        elif len(num) == 3:
            found_digits[num] = 7
            found_digits[7] = num
            l.remove(num)
        elif len(num) == 7:
            found_digits[num] = 8
            found_digits[8] = num
            l.remove(num)

    # Find 3 from 1.
    for num in l:
        if len(num) == 5 and all([c in num for c in found_digits[1]]):
            found_digits[num] = 3
            found_digits[3] = num
            l.remove(num)
            print(f'3 = {num}')
            break

    # Find 9 from 3.
    for num in l:
        if len(num) == 6 and all([c in num for c in found_digits[3]]):
            found_digits[num] = 9
            found_digits[9] = num
            l.remove(num)
            break

    # Find 0 from 7.
    for num in l:
        if len(num) == 6 and all([c in num for c in found_digits[7]]):
            found_digits[num] = 0
            found_digits[0] = num
            l.remove(num)
            break

    # Find remaining 6.
    for num in l:
        if len(num) == 6:
            found_digits[num] = 6
            found_digits[6] = num
            l.remove(num)
            break

    # Find 5 from 6.
    for num in l:
        # len is 5 for all elems now
        if all([c in found_digits[6] for c in num]):
            found_digits[num] = 5
            found_digits[5] = num
            l.remove(num)
            break

    # Add remaining 9.
    for num in l:
        if len(num) == 6:
            found_digits[9] = l[0]
            found_digits[l[0]] = 9
            l.remove(num)

    # Add remaining 2.
    found_digits[2] = l[0]
    found_digits[l[0]] = 2
    l.remove(num)

    return int(''.join([str(found_digits[num]) for num in outputs]))

with open('input8') as f:
    lines = f.readlines()

lines = [[''.join(sorted(num)) for num in line.strip().split() if num != '|'] for line in lines]

cumsum = 0
for line in lines:
    e = process_line(line[:10], line[10:])
    print(e)
    cumsum += e
print(cumsum)
