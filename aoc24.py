import numpy as np
import sys
import math


def _input_reader(prog_inp):
    for c in prog_inp:
        yield int(c)


def run_raw(file_name, inp_str, count=14):
    vars = {'w':0, 'x':0, 'y':0, 'z':0}

    with open(file_name) as f:
        lines = [line.strip() for line in f.readlines()]

    inp = _input_reader(prog_input)

    for line in lines[:count * 18]:
        line_split = line.split()
        if len(line_split) == 3:
            instr, a, b = line_split
            try:
                b = int(b)
            except ValueError:
                b = vars[b]
        else:
            instr, a = line_split

        if instr == 'inp':
            vars[a] = next(inp)
        elif instr == 'add':
            vars[a] += b
        elif instr == 'mul':
            vars[a] *= b
        elif instr == 'div':
            vars[a] //= b
        elif instr == 'mod':
            vars[a] %= b
        elif instr == 'eql':
            vars[a] = 1 if vars[a] == b else 0

    if vars['z'] == 0:
        print('VALID NUMBER')

    return vars


def run_python(inp_str, count=14):
    instr_5_x_add = [12,11,13,11,14, -10,11,-9,-3,13, -5,-10,-4,-5]
    instr_15_y_add = [4,11,5,11,14, 7,11,4,6,5, 9, 12,14,14]
    instr_z_div = [1,1,1,1,1,26,1,26,26,1,26,26,26,26]
    assert len(instr_5_x_add) == 14
    assert len(instr_z_div) == 14
    assert len(instr_15_y_add) == 14

    z = 0

    for i,c in enumerate(inp_str[:count]):
        w = int(c)
        
        if (z % 26) + instr_5_x_add[i] == w:
            z //= instr_z_div[i]
        else:
            z //= instr_z_div[i]
            z *= 26
            z += w + instr_15_y_add[i]

    return z


instr_5_x_add = [12,11,13,11,14,-10,11,-9,-3,13, -5,-10,-4,-5]
instr_15_y_add = [4,11,5,11,14, 7,11,4,6,5, 9, 12,14,14]
instr_z_div = [1,1,1,1,1,26,1,26,26,1,26,26,26,26]
def search(z, inp):
    print(inp, z)
    i = len(inp) - 1

    if len(inp) == 14:
        return z == 0

    if np.prod(instr_z_div[i:]) < z:
        return False

    if (z % 26) + instr_5_x_add[i] == int(inp[-1]):
        z //= instr_z_div[i]
    else:
        z //= instr_z_div[i]
        z *= 26
        z += int(inp[-1]) + instr_15_y_add[i]

    for w in range(9, 0, -1):
        c = str(w)
        if search(z, inp + c):
            return True

def start_search():
    for w in range(9, 0, -1):
        if search(0, str(w)):
            return True
    return False

def search2(z, inp):
    i = len(inp) - 1

    if len(inp) == 14:
        print(inp, z)
        return z == 0

    if np.prod(instr_z_div[i:]) < z:
        return False

    if instr_z_div[i] == 26 and not ((z % 26) + instr_5_x_add[i] == int(inp[-1])):
        return False
        
    if (z % 26) + instr_5_x_add[i] == int(inp[-1]):
        z //= instr_z_div[i]
    else:
        z //= instr_z_div[i]
        z *= 26
        z += int(inp[-1]) + instr_15_y_add[i]

    for w in range(9, 0, -1):
        c = str(w)
        if search2(z, inp + c):
            return True

    

#prog_input = '13579246899999'
prog_input = '33333333333333'
assert len(prog_input) == 14
prog_input = sys.argv[1]
#assert len(prog_input) == 14
count = len(prog_input)

#raw_res = run_raw('input24', prog_input, count)
py_res = run_python(prog_input, count)
#search_res = start_search()

print(prog_input, py_res, len(prog_input))
#print(prog_input, raw_res['z'], len(prog_input))
#print(search_res)
if py_res == 0:
    print(prog_input + ' = valid')
    exit(0)

# if raw_res != py_res:
#     raise ValueError('Inconsitent code')
