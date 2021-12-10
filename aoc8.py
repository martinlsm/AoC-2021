import numpy as np

def process_line(inputs, outputs):
    pass

with open('input8') as f:
    lines = f.readlines()

for line in lines:
    l = line.strip().split(' ')
    inputs = l[:l.index('|')
    outputs = l[l.index('|')+1:]
    process_line(l)
