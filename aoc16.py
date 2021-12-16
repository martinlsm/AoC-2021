import numpy as np

class Packet():
    def __init__(self):
        self.subpackets = []
        self.begin = None
        self.end = None
        self.version = None
        self.type_id = None
        self.value = None

def parse_literal(bin_str, start):
    ptr = start
    while bin_str[ptr] != '0':
        ptr += 5
    end = ptr + 5
    return end


def parse_packet(bin_str, start):
    version = bin_str[start:start+3]
    type_id = bin_str[start+3:start+6]
    if type_id == '100': # type_id == 4
        literal_begin = start + 6
        literal_end = parse_literal(bin_str, literal_begin)
        literal_packet = Packet()
        literal_packet.begin = literal_begin
        literal_packet.end = literal_end
        literal_packet.version = version
        literal_packet.type_id = type_id
        literal_packet.value = int(bin_str[literal_begin:literal_end], base=2)

        end_padded = (literal_end + 0b1111) & (~0b1111)
        return (literal_packet,

with open('input16') as f:
    lines = f.readlines()
assert len(lines) == 1
line = lines[0].strip()
bin_str = bin(int(line, base=16))[2:]
