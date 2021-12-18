import numpy as np

class Packet():
    def __init__(self):
        self.subpackets = []
        self.begin = None
        self.end = None
        self.version = None
        self.type_id = None
        self.value = None

    def __str__(self):
        return self.str_nested(0)

    def __repr__(self):
        return self.str_nested(0)
        
    def str_nested(self, depth):
        pfx = '  ' * depth
        s = f'{pfx}V: 0b{self.version} ({int(self.version, base=2)})\n'
        s += f'{pfx}T: 0b{self.type_id} ({int(self.type_id, base=2)})\n'

        if self.type_id == '100':
            s += pfx + f'L: 0b{self.value} ({int(self.value, base=2)})\n'

        if len(self.subpackets) > 0:
            s += pfx + '{\n'
            for subpacket in self.subpackets:
                s += subpacket.str_nested(depth + 1)
            s += pfx + '}\n'

        return s


def parse_literal(bin_str, start):
    ptr = start
    value = ''
    while True:
        value += bin_str[ptr+1:ptr+5]
        if bin_str[ptr] == '0':
            break
        ptr += 5
    end = ptr + 5
    return (value, end)


def parse_packet(bin_str, start):
    version = bin_str[start:start+3]
    type_id = bin_str[start+3:start+6]
    if type_id == '100': # type_id == 4
        literal_begin = start + 6
        literal_value,literal_end = parse_literal(bin_str, literal_begin)
        end_padded = (literal_end + 0b1111) & (~0b1111)

        literal_packet = Packet()
        literal_packet.begin = literal_begin
        literal_packet.end = end_padded
        literal_packet.version = version
        literal_packet.type_id = type_id
        literal_packet.value = literal_value

        return (literal_packet, end_padded)

with open('singlepacket') as f:
    lines = f.readlines()
assert len(lines) == 1
line = lines[0].strip()
bin_str = bin(int(line, base=16))[2:]

packet,packet_end = parse_packet(bin_str, 0)

print(packet)
