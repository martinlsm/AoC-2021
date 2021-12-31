from collections import deque
import re

def explode(n):
    s = deque()
    depth = 0
    explode_index = None
    explode_end = None
    exploded_left_num = None
    exploded_right_num = None
    leftmost_num_of_exploded_val = None
    leftmost_num_of_exploded_start = None
    leftmost_num_of_exploded_end = None
    rightmost_num_of_exploded_val = None
    rightmost_num_of_exploded_start = None
    rightmost_num_of_exploded_end = None

    for i,c in enumerate(n):
        assert depth >= 0 and depth <= 4

        if c == '[' and depth == 4: # Will explode
            explode_index = i 
            
            # find left explode num
            m = re.search('\\d+', n[explode_index:])
            exploded_left_num = int(m[0])
            d = explode_index + m.end(0)
            
            # find right explode num
            m = re.search('\\d+', n[d:])
            exploded_right_num = int(m[0])
            explode_end = d + m.end(0) + 1
            
            # find leftmost num
            m = None
            for m in re.finditer('\\d+', n[:explode_index]): pass
            if m is not None:
                leftmost_num_of_exploded_val = int(m[0])
                leftmost_num_of_exploded_start = m.start(0)
                leftmost_num_of_exploded_end = m.end(0)

            # find rightmost num
            try:
                m = next(re.finditer('\\d+', n[explode_end:]))
            except:
                pass
            else:
                rightmost_num_of_exploded_val = int(m[0])
                rightmost_num_of_exploded_start = m.start(0) + explode_end
                rightmost_num_of_exploded_end = m.end(0) + explode_end

            #assert n[explode_end - 1] == ']'
            break
        if c == '[':
            depth += 1
        elif c == ']':
            depth -= 1

    if explode_index is None:
        # Did not explode
        return False,n

    # Build result
    if leftmost_num_of_exploded_val is not None:
        new_val = leftmost_num_of_exploded_val + exploded_left_num
        res = n[:leftmost_num_of_exploded_start] + str(new_val) + n[leftmost_num_of_exploded_end:explode_index] + '0'
    else:
        res = n[:explode_index] + '0'

    if rightmost_num_of_exploded_val is not None:
        new_val = rightmost_num_of_exploded_val + exploded_right_num
        res += n[explode_end:rightmost_num_of_exploded_start] + str(new_val) + n[rightmost_num_of_exploded_end:]
    else:
        res += n[explode_end:]

    return True, res


def split(n):
    m = re.search('\\d\\d+', n)
    if m is not None:
        val = int(m[0])
        split_elem = f'[{val // 2},{(val + 1) // 2}]'
        begin = m.start(0)
        end = m.end(0)
        res = n[:begin] + split_elem + n[end:]
        return True, res
    else:
        return False, n


def add(n1, n2):
    res = '[' + n1 + ',' + n2 + ']'

    while True:
        changed,res = explode(res)
        if changed:
            continue
        changed,res = split(res)
        if changed:
            continue
        break

    return res

def split2(n):
    assert n[0] == '['
    depth = 0
    for i,c in enumerate(n):
        if c == '[':
            depth += 1
        elif c == ']':
            depth -= 1
        elif c == ',' and depth == 1:
            d = i
    return n[1:d],n[d+1:-1]


def magnitude(n):
    m = re.match('\\d+', n)
    if m is not None:
        return int(m[0])

    fst,snd = split2(n)
    return 3 * magnitude(fst) + 2 * magnitude(snd)


with open('input18') as f:
    lines = [line.strip() for line in f.readlines()]

num = lines[0] 
for line in lines[1:]:
    num = add(num, line) 

mag = magnitude(num)

print(f'Part 1: {mag}')

max_mag = -1
for n1 in lines:
    for n2 in lines:
        if n1 is n2:
            continue

        mag = magnitude(add(n1, n2))
        if mag > max_mag:
            max_mag = mag

print(f'Part 2: {max_mag}')

