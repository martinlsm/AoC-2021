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
        s += pfx + f'R: {self.eval()}\n'

        if len(self.subpackets) > 0:
            s += pfx + 'S: {\n'
            for subpacket in self.subpackets:
                s += subpacket.str_nested(depth + 1) + '\n'
            s += pfx + '}\n'

        return s

    def version_sum(self):
        return int(self.version, base=2) + sum((p.version_sum() for p in self.subpackets))

    def _op_func(type_id):
        if type_id == '000':
            return lambda ps: np.sum([p.eval() for p in ps])
        elif type_id == '001':
            return lambda ps: np.product([p.eval() for p in ps])
        elif type_id == '010':
            return lambda ps: np.min([p.eval() for p in ps])
        elif type_id == '011':
            return lambda ps: np.max([p.eval() for p in ps])
        elif type_id == '101':
            return lambda ps: int(ps[0].eval() > ps[1].eval())
        elif type_id == '110':
            return lambda ps: int(ps[0].eval() < ps[1].eval())
        elif type_id == '111':
            return lambda ps: int(ps[0].eval() == ps[1].eval())
        else:
            raise ValueError('Not a valid op func')

    def eval(self):
        if self.type_id == '100': # literal
            return int(self.value, base=2)
        else:
            op_func = Packet._op_func(self.type_id)
            return op_func(self.subpackets)


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
    if type_id == '100': # type_id = 4: Literal
        literal_begin = start + 6
        literal_value,literal_end = parse_literal(bin_str, literal_begin)

        literal_packet = Packet()
        literal_packet.begin = start
        literal_packet.end = literal_end
        literal_packet.version = version
        literal_packet.type_id = type_id
        literal_packet.value = literal_value
        return (literal_packet, literal_end)
    else: # Operator
        length_type_id = bin_str[start + 6]
        if length_type_id == '0': # next 15 bits represent total length in bits
            subpackets_length = int(bin_str[start + 7:start + 7 + 15], base=2)
            subpackets_start = start + 7 + 15
            subpackets_end = subpackets_start + subpackets_length 

            subpackets = []
            next_subpacket_start = subpackets_start
            while next_subpacket_start < subpackets_end:
                subpacket,subpacket_end = parse_packet(bin_str, next_subpacket_start)
                subpackets.append(subpacket)
                next_subpacket_start = subpacket_end
            assert next_subpacket_start == subpackets_end

            operator_packet = Packet()
            operator_packet.begin = start
            operator_packet.end = subpackets_end
            operator_packet.version = version
            operator_packet.type_id = type_id
            operator_packet.subpackets = subpackets
            return (operator_packet, subpackets_end)
        else: # next 11 bits number of sub-packets immediately contained by this packet
            subpackets_count = int(bin_str[start + 7:start + 7 + 11], base=2)
            
            subpackets = []
            next_subpacket_start = start + 7 + 11
            for _ in range(subpackets_count):
                subpacket,subpacket_end = parse_packet(bin_str, next_subpacket_start)
                subpackets.append(subpacket)
                next_subpacket_start = subpacket_end

            operator_packet = Packet()
            operator_packet.begin = start
            operator_packet.end = subpacket_end
            operator_packet.version = version
            operator_packet.type_id = type_id
            operator_packet.subpackets = subpackets
            return (operator_packet, subpacket_end)


with open('input16') as f:
    lines = f.readlines()
assert len(lines) == 1
line = lines[0].strip()
bin_str = ''
for c in line:
    b = bin(int(c, base=16))[2:]
    b = ('0' * (-len(b) % 4)) + b
    bin_str += b

packet,packet_end = parse_packet(bin_str, 0)

print(f'Part 1: {packet.version_sum()}')
print(f'Part 2: {packet.eval()}')
